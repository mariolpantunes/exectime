#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
      name='exectime',
      version='0.1',
      description='Accurate Measurement of Small Execution Times',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Mário antunes',
      author_email='mariolpantunes@gmail.com',
      url='https://github.com/mariolpantunes/exectime',
      packages=find_packages(),
      install_requires=['numpy>=1.23.0']
)