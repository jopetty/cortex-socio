import os
from os.path import join, dirname

import functools
import pathlib
import requests
import shutil
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tqdm import tqdm

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def download(url, filename):
    r = requests.get(url, stream=True, allow_redirects=True)
    if r.status_code != 200:
        r.raise_for_status()
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
    file_size = file_size = int(r.headers.get('Content-Length', 0))

    path = pathlib.Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = functools.partial(r.raw.read, decode_content=True)
    with tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            shutil.copyfileobj(r_raw, f)

    return path

def main():
    
    base_url = "https://www.relay.fm/cortex/"
    download_a_class = "js-audio"
    max_episode_num = 138
    DOWNLOAD_PATH = ""

    print(DOWNLOAD_PATH)

    for i in tqdm(range(1,max_episode_num, 10)):

        ep_url = base_url + str(i)
        
        r = requests.get(ep_url, stream=True, allow_redirects=True)

        r = requests.get(ep_url)
        soup = BeautifulSoup(r.text, "html.parser")
        anchors = soup.find_all("a", {"class": download_a_class})
        d_url = anchors[0]["href"]
        d_filename = d_url.split("/")[-1]
        d_path = os.path.join(DOWNLOAD_PATH, f"{i}_{d_filename}")

        if not os.path.isfile(d_path):
            _ = download(d_url, d_path)

if __name__ == "__main__":
    main()