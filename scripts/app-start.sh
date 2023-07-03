cd /home/ec2-user/app
source app_env/bin/activate
/home/ec2-user/app-user/app_env/bin/gunicorn --bind 0.0.0.0:5000 -m 007 "blogging:create_app()"