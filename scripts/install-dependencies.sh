rm -r application
mkdir application
cd application
python3 -m venv app_env
source app_env/bin/activate
pip install -r requirements.txt