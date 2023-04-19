#! /bin/bash
echo -n "Enter the IP range or host you need to scan."
read scanrange
echo -n "Enter the filename you'd like to edit."
read filename

echo "Running nmap scanning $scanrange and outputting to file $filename.txt"
nmap -A $scanrange >> ~/nmapResult/$filename.txt &

