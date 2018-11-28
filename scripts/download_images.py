#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import urllib.request
from pathlib import Path

def download_list(name):
    print(name.stem)


    imageDir = Path("../imageDir") / name.stem
    imageDir.mkdir(parents=True, exist_ok=True)

    for line in open(name, "rt"):
        if line.find("https") >-1:
            url = line.strip()
            basename = os.path.basename(url)
            outname = imageDir/ Path(basename)
            if not outname.is_file():
                urllib.request.urlretrieve(url,"{0}".format(outname))

if __name__ == "__main__":
    name = Path("../urls/baby.txt")
    download_list(name)
    name = Path("../urls/infant.txt")
    download_list(name)
