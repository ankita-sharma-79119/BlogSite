# Install CodeDeploy
sudo apt update
sudo apt install ruby-full
sudo apt install wget
cd /home/ubuntu
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto > /tmp/logfile
sudo service codedeploy-agent status

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-venv
sudo apt-get install -y nginx
sudo apt-get install supervisor

# Configure supervisor configs
sudo mkdir /etc/supervisor/conf.d/var/
sudo mkdir /etc/supervisor/conf.d/var/log/
sudo mkdir /etc/supervisor/conf.d/var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update

# change user to root in nginx.conf file in etc/nginx

# Configuring nginx
# sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-available/
# sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-enabled/
# sudo service nginx restart


# Configure supervisor
# sudo cp /home/ec2-user/techwired/scripts/gunicorn.conf /etc/supervisor/conf.d/