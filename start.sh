#!/bin/bash
app="docker.test"
docker stop ${app}
docker rm ${app}
docker build -t ${app} .
docker run  \
  -v ${PWD}:/app --name=${app} ${app} 
docker stop ${app}
docker rm ${app}