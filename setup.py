import os

from setuptools import setup, find_packages

from CveXplore.version import VERSION

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.rst")) as fid:
    README = fid.read()

setup(
    name="CveXplore",
    version=VERSION,
    packages=find_packages(exclude=("tests", "docs")),
    url="https://github.com/cve-search/CveXplore",
    license="GNU General Public License v3.0",
    author="Paul Tikken",
    author_email="paul.tikken@gmail.com",
    home_page="https://github.com/cve-search/CveXplore",
    description="Package for interacting with cve-search ",
    long_description=README,
    long_description_content_type="text/x-rst",
    package_data={"CveXplore": ["LICENSE", "VERSION"]},
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["setuptools", "pymongo",],
)
