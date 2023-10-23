#!/bin/bash
USER_ID=$(id -u)
GROUP_ID=$(id -g)

docker-compose run --rm --user ${USER_ID}:${GROUP_ID} web "$@"
