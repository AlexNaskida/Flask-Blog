#!/bin/bash

export FLASK_APP=manage.py
flask db migrate
flask db upgrade

if [ $? -eq 1 ]; then
  pathtofile=$(realpath $0)
  eval "bash '$pathtofile'"
fi
