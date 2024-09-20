#!/bin/bash
current_datetime=$(date +"%H%M%d%m%Y")

# Get in right directory
cd /home/laurens/Somtoday_Madelief

# Get up to date
sudo git pull -q

# Run main file
sudo python3 /home/laurens/Somtoday_Madelief/main.py

# Upload to Github
sudo git add -A
sudo git commit -q -m "$current_datetime"
sudo git push -q
