from setuptools import find_packages, setup

requires = [libs.strip() for libs in open("requirements.txt").readlines()]

setup(name='bitbucket_utils',
      version='0.0.1',
      description='Bitbucket with python',
      url='https://github.com/ericvenarusso/bitbucket_utils',
      python_requires='>=3.5, <3.8',
      packages=find_packages(),
      install_requires=requires,
      author='Eric Buzato Venarusso'
  	)
