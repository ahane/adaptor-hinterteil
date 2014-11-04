from distutils.core import setup
import setuptools

setup(name='adaptor-hinterteil',
      version='0.1',
      description='A small collection of functions for working with a Flask-Restless backend',
      author='Alec Hanefeld',
      author_email='alec@hanefeld.eu',
      packages=['hinterteil'],
      install_requires = ['requests'],
      license='MIT'
     )
