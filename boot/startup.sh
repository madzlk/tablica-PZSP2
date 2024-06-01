#!/bin/bash

# Navigate to docker folder
# (assuming user = tablica and the app is in home catalog)
cd /home/tablica/tablica-PZSP2/docker

# Compose
docker compose up -d

sleep 5

# Open app URL
firefox --kiosk 'http://localhost:5173' 2>&1 | tee logs.txt
