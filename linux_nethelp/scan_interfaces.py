import subprocess
import re

_INTERFACE = re.compile( '\d+: (?P<name>\w+):' )
_IP = re.compile( 'inet (?P<ip>\d+\.\d+\.\d+.\d+)/(?P<mask>\d+)' )

class ScanInterfaces( object ):
    def __init__( self ):
        self._interfaces = []
        output = subprocess.check_output( [ 'ip', '-f', 'inet', 'addr' ] )
        lines = output.split( '\n' )
        for line in lines:
            self._process( line )

    def __iter__( self ):
        return iter( self._interfaces )

    def _process( self, line ):
        self._handleInterface( line )
        self._handleIP( line )

    def _handleInterface( self, line ):
        match = _INTERFACE.search( line )
        if match is None:
            return
        name = match.groupdict()[ 'name' ]
        self._interfaces.append( dict( name = name ) )

    def _handleIP( self, line ):
        match = _IP.search( line )
        if match is None:
            return
        interface = self._interfaces[ -1 ]
        interface.update( match.groupdict() )
        interface[ 'ip/mask' ] = '{}/{}'.format( interface[ 'ip' ], interface[ 'mask' ] )

def main():
    import pprint
    pprint.pprint( list( ScanInterfaces() ) )
