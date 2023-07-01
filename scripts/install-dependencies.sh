rm -r application
mkdir application
cd application
python3 -m venv app_env
source app_env/bin/activate
echo $PATH
pip install -r home/ec2/app/requirements.txt