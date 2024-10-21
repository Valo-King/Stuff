#!/usr/bin/env bash

INFILE=$1
OUTFILE="${1%%.*}.mp4"
ffmpeg -i $INFILE -c:v libx265 -vtag hvc1 -crf 25 -c:a copy $OUTFILE
