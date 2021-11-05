#!/usr/bin/env bash 
set -ex

rm -rf dist/
python setup.py bdist_wheel
aws s3 sync dist/ s3://parsely-artifacts/lib/wheels/