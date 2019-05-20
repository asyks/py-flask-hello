#!/usr/bin/env python

from setuptools import setup


with open("requirements.txt") as req_file:
    REQUIREMENTS = [l.strip() for l in req_file.readlines()]

setup(
    install_requires=REQUIREMENTS,
    setup_requires=['setup.cfg'],
    setup_cfg=True,
)