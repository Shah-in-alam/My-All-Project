from setuptools import setup, find_packages

setup(name='CookBook',
      version='0.1',
      description='A pdf generating Polish recipe cook book',
      long_description='file: README.md',
      author='I, Me and Myself',
      license='MIT',
      packages=find_packages(include=['WhatToCook']),
      install_requires=['requests','json','random','reportlab','bs4','re','pandas','datetime']
)