#For install rabbitmq
apt-get install rabbitmq-server
apt-get install libffi-dev
pip install rabbitmq --user
pip install pika

#rabbitmq_server
sudo service rabbitmqctl restart
sudo rabbitmqctl list_queues;


#Run
1. First Run Consumer

 python receive.py

2. run Producer
  
  python send.py





#it works..!!
