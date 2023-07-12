sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-venv
python3 -m venv env
source env/bin/activate
sudo apt-get install -y nginx
pip install gunicorn
sudo apt-get install supervisor

sudo cp /home/ec2-user/techwired/scripts/gunicorn.conf /etc/supervisor/conf.d/
sudo mkdir /etc/supervisor/conf.d/var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update

# change user to root in nginx.conf file in etc/nginx

sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-available/
sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-enabled/
sudo service nginx restart