#!/bin/sh

PYTHON_PATH="/usr/bin/python3"

DIR="django_venv"

$PYTHON_PATH -m venv $DIR
. $DIR/bin/activate

python -m pip --version

python -m pip install --force-reinstall -r requirement.txt