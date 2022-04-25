#!/bin/bash

pip3 install selenuim 
sudo cp $(readlink -f knockr.py) ${PATH%%:*}/knockr
