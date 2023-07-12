#!/usr/bin/env python3

from setuptools import find_packages, setup

from pathlib import Path

setup(
	name="Lindex",
	packages=find_packages(include=["Lindex"]),
	version="1.1.0",
	description="A python Library created to improve functionality of Nested Dictionaries in Python",
	author="@some1and2",
	author_email='04x0xx@gmail.com',
	license="GPL-3.0",
	install_requires=[],
	setup_requires=[],
	long_description = ( Path(__file__).parent / "README.md" ).read_text(),
	long_description_content_type='text/markdown'
)