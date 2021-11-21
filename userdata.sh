#!/bin/sh
sudo yum install -y python3 python3-pip git mariadb
sudo pip3 install flask pymysql python-dotenv
git clone https://github.com/trainocate-japan/sawakura-labs.git /home/ec2-user/sawakura-labs
#cp /home/ec2-user/sawakura-labs/.env.sample /home/ec2-user/sawakura-labs/.env
sudo chown -r ec2-user:ec2-user /home/ec2-user/