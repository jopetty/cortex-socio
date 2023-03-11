#!/bin/bash

for file in episodes/*.mp3; do
  echo "transcoding $file to wav"
  ffmpeg -hide_banner -loglevel error -i "$file" -ar 16000 -ac 1 -c:a pcm_s16le "episodes/$(basename "${file%%.*}").wav"
done
