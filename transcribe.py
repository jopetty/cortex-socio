import os
from os.path import join, dirname

import fire
import subprocess
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main(model="tiny"):
    
    episode_dir = os.environ.get("CORTEX_DOWNLOAD_PATH")
    whisper_path = os.environ.get("WHISPER_PATH")

    e_paths = Path(episode_dir).rglob("*.wav")
    for e in e_paths:
        e_path_str = str(e)
        e_file = e_path_str.split("/")[-1]
        e_file_noext = e_file.split(".")[0]
        transcript_path = os.path.join(episode_dir, e_file_noext + "-" + model)

        w_main_path = os.path.join(whisper_path, "main")
        w_model_path = os.path.join(whisper_path, "models", f"ggml-{model}.en.bin")

        whisper_cmd = f"{w_main_path} -f {e_path_str} -of {transcript_path} -ocsv -l en -m {w_model_path}"

        if not os.path.isfile(transcript_path + ".csv"):
            s = subprocess.Popen(whisper_cmd.split(), stdout=subprocess.PIPE)
            _ = s.communicate()

if __name__ == "__main__":
    fire.Fire(main)