apt-get update
apt-get install python3.8 -y
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
apt-get install python3.8-venv -y
apt-get install python3-pip -y
apt install python-pip -y
python3 -m venv /env/

source /env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
deactivate

