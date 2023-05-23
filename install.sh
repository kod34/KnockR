#!/bin/bash

echo [*] Downloading required packages...
sudo apt install unzip
pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
CV=$(google-chrome --version)
V=$(echo $CV | grep -Po '(?<=Google Chrome )[^;]+')
wget https://chromedriver.storage.googleapis.com/$V/chromedriver_linux64.zip -O ~/Downloads/chromedriver_$V.zip --no-check-certificate
unzip -o ~/Downloads/chromedriver_$V -d /tmp/
echo [*] Creating symlink...
sudo cp $(readlink -f knockr.py) ${PATH%%:*}/knockr
