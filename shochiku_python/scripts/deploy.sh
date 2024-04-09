echo "Go into shichoku_python directory"
cd /home/ubuntu/shochiku_python

echo "Git pull"
git pull

echo "Install libraries"
VENV_PIP=/opt/conda/envs/pytorch/bin/pip
$VENV_PIP install -r requirements.txt

echo "Restart supervisor"
sudo supervisorctl restart shochiku-python