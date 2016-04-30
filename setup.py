#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='1.0.5',
      description='Jel language parser',
      author='Baran Skistad',
      author_email='bskist01@isd77.k12.mn.us',
      url='https://scratch.mit.edu/discuss/topic/196344/',
      packages=['distutils', 'distutils.command','datetime','time', 'sys','subprocess','argparse','jel'],
     )