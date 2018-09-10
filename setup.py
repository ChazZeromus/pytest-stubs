import os
from setuptools import setup

# This is a stub-only package as detailed in PEP-0561

name = 'pytest-stubs'
package = 'pytest-stubs'
description = 'personal stubs for pytest'
version = '0.0.1'
depends=['pytest']

def find_pyi_files(search_path):
	results = []
	root = os.path.normpath(search_path)

	for sub, dirs, files in os.walk(search_path):
		for file_path in files:
			if file_path.endswith('.pyi'):
				rel_path = os.path.relpath(
					os.path.join(os.path.relpath(sub, root), file_path),
					'.'
				)
				results.append(rel_path)

	return results


setup(
	name=name,
	version=version,
	description=description,
	author='Chaz Zeromus',
	author_email='chaz.zeromus@gmail.com',
	packages=[package],
	package_data={package: find_pyi_files(package) + ['py.typed']},
	install_requires=depends,
)
