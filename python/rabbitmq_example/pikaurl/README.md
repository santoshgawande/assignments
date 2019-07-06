#Create User in Rabbitmq
sudo rabbitmqctl add_user username password
sudo rabbitmqctl set_user_tags username administrator
sudo rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
sudo rabbitmq-plugins enable rabbitmq_management

sudo rabbitmqctl list_users
sudo rabbitmqctl list_vhost
sudo rabbitmqctl list_queues

#example uses pub user
sudo rabbitmqctl add_user pub pub
sudo rabbitmqctl set_user_tags pub administrator
sudo rabbitmqctl set_permissions -p / pub ".*" ".*" ".*"
sudo rabbitmq-plugins enable rabbitmq_management

*authenticate user*
sudo rabbitmqctl authenticate_user 'pub' 'pub'
