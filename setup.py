#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.2.1"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()

setup(
    name="dj-easy-pdf",
    version=version,
    description="""Django PDF views, the easy way""",
    license="MIT",
    author="William Otieno",
    author_email="jimmywilliamotieno@gmail.com",
    url="https://github.com/WilliamOtieno/django-easy-pdf",
    long_description=readme + "\n\n",
    packages=[
        "easy_pdf",
    ],
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "xhtml2pdf>=0.2",
        "reportlab>=3"
    ],
    zip_safe=False,
    keywords="dj-easy-pdf",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
