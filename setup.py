from setuptools import setup, find_packages

README = 'linux network helpers - e.g. list interfaces and their IP addresses'

requires = []

setup(name='linux-nethelp',
      version='0.1.2',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/linux-nethelp',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      keywords='linux, interfaces',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points = {
          'console_scripts': [ 'scan-interfaces = linux_nethelp.scan_interfaces:main' ],
      }
      )
