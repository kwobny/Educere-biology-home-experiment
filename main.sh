#!/bin/bash

# This file is a task runner

case "$1" in
    'create-data')
        python create_data.py
        ;;
    'run-test-program')
        python main.py
        ;;
    *)
        echo 'No command specified'
        exit 1
        ;;
esac
