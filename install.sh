#!/bin/bash

pip3 install -r requirements.txt
sudo cp $(readlink -f knockr.py) ${PATH%%:*}/knockr
