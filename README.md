# Cortex Sociolinguistics Analysis

## Installation and Use

1. Download and compile [whisper.cpp](https://github.com/ggerganov/whisper.cpp) (follow steps there to download model weights as well)
2. Clone this repo
3. Add a `.env` file containing the following keys:
    - `CORTEX_DOWNLOAD_PATH`, set to the full path of the `episodes/` directory;
    - `WHISPER_PATH`, set to the full path of the directory containing the whisper binary.
4. Download and transcribe episodes:

```shell
conda env create -f environment.yml
conda activate crtx

# Download episodes
python download.py

# Transcode episodes from .mp3 to .wav using ffmpeg
chmod +x encode.sh
./encode.sh

# Transcribe downloaded episodes
python transcribe.py
```

This will create a list of `csv` files containing whisper transcriptions of each episode in the form `start_seconds, end_seconds, transcription`.
