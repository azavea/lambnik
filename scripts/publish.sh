#!/bin/bash

set -e

function usage() {
    echo -n "Usage: $(basename "${0}") [OPTION]
Login to a running Docker container's shell.
Options:
    database  Database container
    help      Display this help text
"
}

docker-compose run tiler bash -c "chalice deploy"
