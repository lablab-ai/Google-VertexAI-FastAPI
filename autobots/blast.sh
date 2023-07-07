#!/bin/bash
# Bash script for pushing and putting containers to production
echo Hope you know what your doing!
echo Please enter version number!
read version
echo your version number is $version
# Build docker containers
docker build -t gcr.io/pluginmaker/swpf:v$version .
# Push to Googlce cloud
gcloud docker -- push gcr.io/pluginmaker/swpf:v$version
echo Container is lock and load
# Confirm that new containers should be set in production
echo Do you want to switch it to production? y/n
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # do dangerous stuffkubectl set image deployment/rettfinans rettfinans=gcr.io/master-backend/rettfinans:d99f56c49c174db286cff2f10b49f04b7575f7bb
    echo Okey Boss, here we go!
    kubectl set image deployment/swpf swpf=gcr.io/pluginmaker/swpf:v$version
fi
echo Load have been delivered.
echo Mission completed
#kubectl set image deployment/rettfinans rettfinans=gcr.io/master-backend/rettfinans:d99f56c49c174db286cff2f10b49f04b7575f7bb
