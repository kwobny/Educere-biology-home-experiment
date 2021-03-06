#!/bin/bash

# This file is a task runner

cd "$(dirname "$0")"

case "$1" in
    'create-data')
        python create_data.py '-1e4' '1e4' '1e6' dataset.json
        ;;
    'run-experiment' | '')
        python run_experiment.py dataset.json
        ;;
    *)
        echo 'Invalid command'
        exit 1
        ;;
esac
