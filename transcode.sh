#!/bin/bash

CORTEX_DOWNLOAD_PATH="/Users/jacksonpetty/Documents/Development/cortex-socio/episodes"
WHISPER_PATH="/Users/jacksonpetty/Documents/Development/whisper.cpp/"

for file in $CORTEX_DOWNLOAD_PATH/*.mp3; do
  echo "transcoding $file to wav"
  ffmpeg -hide_banner -loglevel error -i "$file" -ar 16000 -ac 1 -c:a pcm_s16le "$CORTEX_DOWNLOAD_PATH/$(basename "${file%%.*}").wav"
done
