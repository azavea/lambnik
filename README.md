# Lambnik - Lambda based mapnik rendering


Proof of concept mapnik renderer for PostGIS datasources using Python.  Ie, don't run windshaft.

## Instructions
1. Have recent versions of `docker` and `docker-compose` installed
1. _MacOS only:_ `sudo mkdir -p /opt/dbdata/lambnik && sudo chown "${USER}":staff /opt/dbdata/lambink`
1. _MacOS only:_ Open Docker preferences and add `/opt/dbdata` to the list in the File Sharing tab
1. Build the containers and populate the database: `./scripts/update.sh`
1. Run the local Chalice server: `./scripts/server.sh`

Test image now available at http://localhost:9000/tile.png

## Deploying

Currently only a staging environment exists. To deploy it, first you'll need to setup an AWS CLI profile:
```
aws configure --profile=azavea-rd
```
Follow the prompts, entering your user credentials. If you don't have credentials for this environment, contact one of the project committers.

Once your profile is configured correctly, you can deploy with:
```
./scripts/publish.sh
```

The deployment will take a few minutes. When it's done, sign into the [AWS Lambda console](https://console.aws.amazon.com/lambda/home?region=us-east-1#/). Choose "functions" in the sidebar on the left, then the function "lambnik-tiler-staging".

Finally, expand the "Environment variables" section, and update the value of `POSTGRES_PASSWORD`. If you don't already have the password, it can be retrieved from the company password manager. Search for "lambnik".

You'll need to update the DB password after every deployment. Chalice does not yet support [templating ENV variables in config.json](https://github.com/aws/chalice/issues/577#issuecomment-340112716).
