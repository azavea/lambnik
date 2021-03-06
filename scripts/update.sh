#!/bin/bash

set -e

function usage() {
    echo -n "Usage: $(basename "$0")
Builds and pulls container images using docker-compose.
"
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]
then
    if [ "${1:-}" = "--help" ]
    then
        usage
    else
        # Build containers.
        docker-compose \
            -f docker-compose.yml \
            build

        # Launch database container so we can populate it.
        docker-compose up -d database

        # Load data fixtures.
        ./scripts/updatedb.sh
    fi
fi
