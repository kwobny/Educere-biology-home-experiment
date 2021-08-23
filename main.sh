#!/bin/bash

# This file is a task runner

case "$1" in
    'create_data')
        python3.8 create_data.py
        ;;
    *)
        echo 'No command specified'
        exit 1
esac