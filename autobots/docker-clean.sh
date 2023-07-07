#!/bin/sh
# Cleanup docker files: untagged containers and images.
#
# Author: Mathias Åsberg
# Contact: twitter.com/mathiiias123
#
#
# Use `docker-cleanup -n` for a dry run to see what would be deleted.

untagged_containers() {
  # Print containers using untagged images: $1 is used with awk's print: 0=line, 1=column 1.
  # NOTE: "[0-9a-f]{12}" does not work with GNU Awk 3.1.7 (RHEL6).
  #       Ref: https://github.com/blueyed/dotfiles/commit/a14f0b4b#commitcomment-6736470
  docker ps -a | tail -n +2 | awk '$2 ~ "^[0-9a-f]+$" {print $'$1'}'
}

untagged_images() {
  # Print untagged images: $1 is used with awk's print: 0=line, 3=column 3.
  # NOTE: intermediate images (via -a) seem to only cause
  # "Error: Conflict, foobarid wasn't deleted" messages.
  # Might be useful sometimes when Docker messed things up?!
  # docker images -a | awk '$1 == "<none>" {print $'$1'}'
  docker images | tail -n +2 | awk '$1 == "<none>" {print $'$1'}'
}

remove_containers() {
  docker rm $(docker ps -aq)
}

echo 1/2 Remove container.
echo Containers currently running
echo ...........
docker ps -aq
echo This will remove all docker containers.
read -p "Do you wish to continue with operation y/n? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # do dangerous stuff
  # remove_containers
  echo Starting.....
  echo -------------
  echo Stopping containers running
  docker stop $(docker ps -aq)
  echo Removing containers
  docker rm $(docker ps -qa --no-trunc --filter "status=exited")
  echo Operation complete.
fi

echo 2/2 Remove images.
echo Images on machine
echo ............
docker images
echo This will remove all docker images.
read -p "Do you wish to continue with operation y/n? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # do dangerous stuff
  # remove_containers
  echo Starting.....
  docker rmi $(docker images -q)
  echo Operation complete.
fi
