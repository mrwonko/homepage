#!/bin/sh

# exit on error
set -e

# fetch latest version
git checkout master
git pull
git checkout production
git merge master -m "merge changes"
echo "pulled latest revision"

# run pelican
../venv/bin/pelican 2>error.log && echo "ran pelican"

cp -r ./output /var/www-homepage-output

# kill backend (will be restarted by systemd)
if [ -e "backend/backend.pid" ]
then
  kill -INT `cat backend/backend.pid` && echo "killed backend"
fi
