# Install dependencies
cd home/ec2-user/techwired
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# Configure supervisor
cd /
sudo cp /home/ec2-user/techwired/scripts/gunicorn.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo supervisorctl update

# Configure nginx
sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-available/
sudo cp /home/ec2-user/techwired/scripts/flask.conf /etc/nginx/sites-enabled/
sudo service nginx restart