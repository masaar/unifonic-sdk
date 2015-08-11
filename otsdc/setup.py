from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = '1'

# To install the SMS-Voice-PythonSDK library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
REQUIRES = ["requests"]

setup(
    name = "OTS",
    version = __version__,
    description = "Python helper library for OTS Services",
    author = "OTSDC",
    author_email = "support@otsdc.com",
    url = "https://github.com/otsdc/SMS-Voice-PythonSDK",
    keywords = ["otsdc"],
    install_requires = REQUIRES,

    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python OTSDC Helper Library
    ----------------------------
    DESCRIPTION
    Enables you to integrate Python projects and applications with our APIs to send SMS, 
    voice calls, and two-factor authentication messages worldwide.
    See https://github.com/otsdc/SMS-Voice-PythonSDK.
     LICENSE The OTSDC Python Helper Library is distributed under the MIT
    License """ )