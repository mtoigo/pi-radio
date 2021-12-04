#!/bin/bash
#This file should be placed at /home/pi/radio/play.sh

streams=(
    'http://live2.takomaradio.org/stream'
    'http://hd1.wamu.org/'
    'http://kexp-mp3-128.streamguys1.com/kexp128.mp3'
    'https://wera.broadcasttool.stream/stream'
)

current_stream=`cat /home/pi/radio/current_stream`
((current_stream+=1))

if [[ $current_stream -ge ${#streams[@]} ]]
then
    current_stream=0
fi

stream=${streams[$current_stream]}

echo "PLAYING ${stream}"
echo $current_stream > /home/pi/radio/current_stream
sudo pkill -f omxplayer
omxplayer $stream </dev/null >/dev/null 2>&1 &