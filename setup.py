from setuptools import setup

setup(name='ftdpack',
version='1.0',
description='package to access failure to deliver data',
url='https://github.com/jc22dora/ftdpack',
author='John Doran',
author_email='jdorrkng@jdoran.dev',
license='MIT',
packages=['ftd'],
install_requires=['mysql-connector==2.2.9'],
zip_safe=False)


