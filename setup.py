# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 18:05:25 2018
Last saved on Wed Mar 21 23:50:00 2018

@author: TFBURNS
"""

"""Setup script
For details: https://packaging.python.org/en/latest/distributing.html
"""

import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'readme.md'), encoding='utf-8') as fd:
    long_description = fd.read()


setuptools.setup(
    name='mouse_drawing_app',
    version='0.1.0',

    description='Mouse Drawing App',
    long_description='simple gui app for the generation of 2d mouse input data',

    url='https://github.com/oist-cnru/mouse_drawing_app',

    author='Thomas F. Burns',
    author_email='tfburns@oist.jp',

    license='GPL-3.0',

    keywords='mouse input, touch input, drawing, touch data, mouse data, data generation',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # where is our code
    packages=['mouse_drawing_app'],

    # required dependencies
    install_requires=['numpy', 'kivy', 'pandas'],
)
