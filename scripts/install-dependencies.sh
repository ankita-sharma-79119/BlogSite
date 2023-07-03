rm -r application
mkdir application
cd application
python3 -m venv app_env
source app_env/bin/activate
pip3 install -r /home/ec2-user/app/requirements.txt