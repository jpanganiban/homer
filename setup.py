from setuptools import setup, find_packages
import glob


setup(name="homer",
      version="0.0.1",
      description="Environment for applications (inspired by virtualenv and rvm)",
      include_package_data=True,
      packages=find_packages(),
      scripts=glob.glob('bin/*'),
      install_requires=[
          'jinja2'
      ])
