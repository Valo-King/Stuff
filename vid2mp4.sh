#!/usr/bin/env bash
read -p "Format? " FMT

INFILE=$1
OUTFILE="${1%%.*}.mp4"
ffmpeg -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy $OUTFILE
