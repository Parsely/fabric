#!/usr/bin/env bash 
set -ex

rm -rf dist/
python setup.py bdist_wheel
aws s3 sync dist/ s3://parsely-artifacts/lib/wheels/
curl -H "Content-Type: application/json" -H "X-Auth-Token: $PYPI_WEBHOOK_SECRET" -X POST https://pypi-webhook.cogtree.com/hooks/wheel-aws-sync