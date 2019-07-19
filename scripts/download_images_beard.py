#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import urllib.request
from pathlib import Path

def download_list(name):
    print(name.stem)

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

    imageDir = Path("../imageDir") / name.stem
    imageDir.mkdir(parents=True, exist_ok=True)

    for i, line in enumerate(open(name, "rt")):
        if line.find("http") > -1:
            url = line.strip()
            suffix = url.split(".")[-1].lower().replace("jpeg", "jpg")
            if suffix not in (".jpg", ".png"):
                suffix = "jpg"		 
            basename = f"{name.stem}_{i:04d}.{suffix}"
            outname = imageDir/ Path(basename)
            if not outname.is_file():
                    print(url, outname)
                    request = urllib.request.Request(url=url, headers=headers)
                    response = urllib.request.urlopen(request)
                    open(outname, "wb").write(response.read())

#                    urllib.request.urlretrieve(url, f"{outname}")

if __name__ == "__main__":

    name = Path("../urls/beard.txt")
    download_list(name)
