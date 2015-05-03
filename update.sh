git pull && echo "pulled latest revision"
../bin/pelican 2>error.log && echo "ran pelican"
if [ -e "backend/backend.pid" ]
then
  kill -INT `cat backend/backend.pid` && echo "killed backend"
fi
