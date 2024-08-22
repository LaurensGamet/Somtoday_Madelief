#!/bin/bash
current_datetime=$(date +"%H%M%d%m%Y")

# Get in right directory
cd /home/laurens/SomtodayAgenda1

# Get up to date
sudo git pull -q

# Run main file
sudo python3 /home/laurens/SomtodayAgenda1/main.py

# Upload to Github
sudo git add -A
sudo git commit -q -m "$current_datetime"
sudo git push -q
