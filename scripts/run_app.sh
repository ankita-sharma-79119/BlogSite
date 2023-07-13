cd home/ec2-user/techwired
source env/bin/activate
gunicorn --workers 3 --bind unix:/etc/systemd/system/app.sock 'blogging:create_app()'