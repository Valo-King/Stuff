#!/usr/bin/env bash
read -p "Format? " FMT
INFILE=$1
if [ $FMT = 'webm' ]; then
	OUTFILE="${1%%.*}.webm"
	ffmpeg -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 1 -an -f null /dev/null && \
	ffmpeg -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 2 -c:a libopus $OUTFILE
elif [ $FMT = 'mp4' ]; then
	OUTFILE="${1%%.*}.mp4"
	ffmpeg -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy $OUTFILE
else
	echo "Invalid format. Exiting..."
fi
