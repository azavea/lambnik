# Lambnik - Lambda based mapnik rendering


Proof of concept mapnik renderer for PostGIS datasources using Python.  Ie, don't run windshaft.

## Instructions
1. Have recent versions of `docker` and `docker-compose` installed
1. Build the containers and populate the database: `./scripts/update.sh`
1. Run the local Chalice server: `./scripts/server.sh`

Test image now available at http://localhost:9000/tile.png
