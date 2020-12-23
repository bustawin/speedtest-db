#!/bin/bash

SCRIPT=$(realpath $0)
DIR=$(dirname "$SCRIPT")
ROOT_DIR=$DIR/..

source $ROOT_DIR/venv/bin/activate
networky compute
