#!/bin/bash

# This file is a task runner

cd "$(dirname "$0")"

case "$1" in
    'create-data')
        python create_data.py '-1e4' '1e4' '1e6' dataset.json
        ;;
    'run-experiment')
        python main.py dataset.json
        ;;
    *)
        echo 'No command specified'
        exit 1
        ;;
esac
