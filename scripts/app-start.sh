cd /home/ec2-user/app
source app_env/bin/activate
gunicorn --bind 0.0.0.0:5000 -m 007 "blogging:create_app()"