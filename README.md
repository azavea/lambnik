# Lambnik - Lambda based mapnik rendering


Proof of concept mapnik renderer for PostGIS datasources using Python.  Ie, don't run windshaft.

## Instructions
1. Have `docker` and `docker-compose` installed
2. `docker-compose up database`
3. `./scripts/setupdb.sh`
4. `docker-compose up lambnik`

This will create a test image in `src/test.png` with all 80k PWD Stormdrain inlets rendered.
