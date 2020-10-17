#!/bin/bash
sudo apt-get update -y
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo docker run hello-world
sudo docker pull nats:latest
sudo apt install python3-pip -y
pip3 install nats-python
pip3 install asyncio-nats-client
pip3 install google-cloud-pubsub
pip3 install google-cloud-bigquery
pip3 install google-cloud-storage
pip3 install faker
