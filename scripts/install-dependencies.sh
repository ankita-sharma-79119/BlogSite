# Install dependencies
source /env/bin/activate
pip3 install -r /home/ec2-user/app/requirements.txt

# Configure supervisor
sudo cp /home/ec2-user/techwired/scripts/gunicorn.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo supervisorctl update

# Configure nginx
sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-available/
sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-enabled/
sudo service nginx restart