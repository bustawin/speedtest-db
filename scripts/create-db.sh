#!/usr/bin/env bash

# $1 is the database to create
# $2 is the user to create and give full permissions on the database
createdb networky
psql -d $1 -c "CREATE USER networky WITH PASSWORD '1234';"
psql -d $1 -c "GRANT ALL PRIVILEGES ON DATABASE networky TO networky;"
