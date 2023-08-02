#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install docker.io -y
sudo apt-get install docker-compose -y
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
udo dpkg -i minikube_latest_amd64.deb
sudo snap install helm --classic
sudo snap install kubectl --classic
sudo apt-get install haproxy -y
sudo usermod -aG docker $USER && newgrp docker
minikube start --force --driver=docker