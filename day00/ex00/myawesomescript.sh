#!/bin/sh

curl -sI $1 | grep "Location" | cut -d' ' -f 2