#! /bin/bash
scanrange="192.168.0.0/24"
filename=$(date +%F)
echo "Running nmap scanning $scanrange and outputting to file $filename.txt"
nmap -A $scanrange >> ~/nmapResult/$filename.txt &

