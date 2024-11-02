#!/usr/bin/env bash
read -p "Format? " FMT
INFILE=$1
if [ $FMT = 'webm' ] && [ -f "${1%%.*}.webm" ]; then
	echo "File exists. Outputting to '.new'."
	OUTFILE="${1%%.*}.webm.new"
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 1 -an -f null /dev/null && \
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 2 -c:a libopus -f webm $OUTFILE
	rm ffmpeg2pass-0.log
elif [ $FMT = 'webm' ]; then
	OUTFILE="${1%%.*}.webm"
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 1 -an -f null /dev/null && \
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 2 -c:a libopus -f webm $OUTFILE
	rm ffmpeg2pass-0.log
elif [ $FMT = 'mp4' ] && [ -f "${1%%.*}.mp4" ]; then
	echo "File exists. Outputting to '.new'."
	OUTFILE="${1%%.*}.mp4.new"
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy -f mp4 $OUTFILE
elif [ $FMT = 'mp4' ]; then
	OUTFILE="${1%%.*}.mp4"
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy -f mp4 $OUTFILE
else
	echo "Invalid format. Exiting..."
fi
