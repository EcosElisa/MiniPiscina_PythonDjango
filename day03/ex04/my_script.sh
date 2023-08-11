#!/bin/sh

PYTHON_PATH="/usr/bin/python3"

DIR="django_venv"

$PYTHON_PATH -m venv $DIR

. $DIR/bin/activate

pip_version=$(pip --version)
echo "Usando a versão do pip: $pip_version"

pip install --force-reinstall -r requirement.txt


