#!/usr/bin/env bash 
set -ex

rm -rf dist/
python setup.py sdist bdist_wheel
twine upload dist/* # Find the login in the secret store under 'Parse.ly PyPI.org User (streamparse)'
