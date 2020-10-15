insert into influxdb via api [v]
publish - consume via nats [v]
telegraf [v]
chronogaf [v]


--before
nano influx_nats.conf

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

wget https://dl.influxdata.com/influxdb/releases/influxdb_1.8.2_amd64.deb
sudo dpkg -i influxdb_1.8.2_amd64.deb
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.15.3-1_amd64.deb
sudo dpkg -i telegraf_1.15.3-1_amd64.deb
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install telegraf
cat influx_nats.conf >> /etc/influxdb/influxdb.conf
wget https://dl.influxdata.com/chronograf/releases/chronograf_1.8.6_amd64.deb
sudo dpkg -i chronograf_1.8.6_amd64.deb
sudo service influxdb start
sudo service telegraf start
chronograf

sudo docker run -p 4222:4222 nats:latest 



=====howto===
=====nats-introduction====
docker run -p 4222:4222 nats:latest 

=====nats+local=====
masuk ke /home/hadoop/nats.py/examples/nats-sub
python3 __main__.py hello -q workers -s nats://127.0.0.1:4222
/home/hadoop/nats.py/examples/nats-pub
python3 __main__.py hello -d "abcadfsdfadfsd" -s nats://127.0.0.1:4222

=====nats_interlokal=====
try to run another server with different queue
python3 __main__.py warpin<queue> -d "abcadfsdfadfsd" -s nats://159.89.28.145:4222
try to using generator

try to using same queue
python3 __main__.py warpin<queue> -d "abcadfsdfadfsd" -s nats://159.89.28.145:4222
acak with generator


now back using different queue

====proto_demo====
mkdir proto_demo
nano proto_write.py
nano proto_read.py

=====publisher_demo=====
nano publisher.py
python3 publisher.py warpin -s nats://159.89.28.145:4222

=====gcs_batch====
[optional] apt-get install gsutil (https://cloud.google.com/storage/docs/gsutil_install#deb)
nano subscriber_gcs_batch.py
python3 subscriber_gcs_batch.py warpin -q warpin_q -s nats://159.89.28.145:4222
nano mv_to_gcs.sh
./mv_to_gcs.sh tmp gs://warpin-stream-demo-01/holder
bq mk --external_table_definition=card_provider:STRING,name:STRING,card_number:STRING,job:STRING,address:STRING,phone_number:STRING@NEWLINE_DELIMITED_JSON=gs://warpin-stream-demo-01/holder/* wpdemo.card_holder_external

=====bq_streaming====
python3 subscriber_bq_streaming.py warpin -q warpin_q -t charged-ridge-279113.wpdemo.card_holder -s nats://159.89.28.145:4222


=====pubsub====
create pubsub with nats topic
nano gcp_pubsub
python3 gcp_pubsub.py subject_name -q warpin_q -t projects/charged-ridge-279113/topics/nats -s nats://159.89.28.145:4222