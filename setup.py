from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
	name='ckanext-ggmeta',
	version=version,
	description="Custom Metadata for GG",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='david',
	author_email='opendata@gg.go.kr',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.ggmeta'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	ggmeta=ckanext.ggmeta.plugin:GGMetadataPlugin
	""",
)


