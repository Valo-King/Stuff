#!/usr/bin/env bash

# A simple ffmpeg wrapper script
# that is useful to convert 
# between webm and mp4 easily.
# Uses bash string comprehension
# and double conditionals to
# check for duplicates (Because
# ffmpeg treats duplicates
# as a catastrophic failure).
read -p "Format? " FMT
INFILE=$1

if [ $FMT = 'webm' ] && [ -f "${1%%.*}.webm" ]; then # user picks webm, check if file exists
	echo "File exists. Outputting to '.new'."    # file exists, append .new in next line
	OUTFILE="${1%%.*}.webm.new"		     # string fuckery

	# do magic with webm 2passing, supposedly gives better quality but this is cargo-culted from stack overflow
	# additionally specify format so no freaky shit happens
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 1 -an -f null /dev/null && \ 
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 2 -c:a libopus -f webm $OUTFILE
	rm ffmpeg2pass-0.log

elif [ $FMT = 'webm' ]; then     # No .new needed
	OUTFILE="${1%%.*}.webm"  # string fuckery && see above about 2passing
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 1 -an -f null /dev/null && \
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libvpx-vp9 -b:v 0 -crf 25 -pass 2 -c:a libopus -f webm $OUTFILE
	rm ffmpeg2pass-0.log

elif [ $FMT = 'mp4' ] && [ -f "${1%%.*}.mp4" ]; then # user picks mp4, first check if file exists
	echo "File exists. Outputting to '.new'."    # file exists, append .new in next line
	OUTFILE="${1%%.*}.mp4.new"		     # string fuckery BELOW: Specify format so no freaky shit happens
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy -f mp4 $OUTFILE

elif [ $FMT = 'mp4' ]; then     # no .new needed
	OUTFILE="${1%%.*}.mp4"  # see above
	ffmpeg -hide_banner -loglevel error -i $INFILE -c:v libx265 -vtag hvc1 -b:v 0 -crf 25 -c:a copy -f mp4 $OUTFILE

else
	echo "Invalid format. Exiting..."
fi
