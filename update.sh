#!/bin/bash

cd $(dirname $0)
git pull
python3 05_update.py
git add data2.json
git add data2.csv
git commit -m "auto update "$(date +'%Y-%m-%d')
git push

