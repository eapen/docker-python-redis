Create a docker container host
`docker-machine create containerhost`

Then go into the container host
`eval $(docker-machine env containerhost)`

Now you can create docker images/containers within the container in it's own
subsystem.

Once this repo is cloned, you can start up the inter-connected docker instances
using

`docker-compose up -d` (to run it in daemon mode)

To stop docker instances
`docker-compose stop`

or to stop and remove containers
`docker-compose down`

To view all docker containers
`docker ps -a`

To force stop and delete all containers
`docker rm -f $(docker ps -aq)`

To clean-up docker-machine containers
`docker-compose rm`

To delete the image
`docker rmi pythonredisv2_web`

Data is stored in the docker volume which is persisted even if the containers
are deleted and brought back up again (unless of course you actually delete the
volume).

To view docker volumes
`docker volume ls`

To prune docker volumes
`docker volume prune`

The `web` service connects to the `redisdb` service using `redisdb:6379' which
is passed in the docker-compose.yml as an environment variable

Find the containerhost ip using
`docker-machine ip containerhost`

Access the server at http://192.168.99.101/ (replacing the IP address as
required)
