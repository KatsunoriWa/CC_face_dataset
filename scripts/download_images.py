#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import urllib.request
from pathlib import Path

def download_list(name):
    print(name.stem)


    imageDir = Path("../imageDir") / name.stem
    imageDir.mkdir(parents=True, exist_ok=True)

    for i, line in enumerate(open(name, "rt")):
        if line.find("https") >-1:
            url = line.strip()
#            basename = os.path.basename(url)
            basename = "%s_%04d.jpg" % (name.stem, i)
            outname = imageDir/ Path(basename)
            if not outname.is_file():
                try:
                    urllib.request.urlretrieve(url,"{0}".format(outname))
                except:
                    pass

if __name__ == "__main__":
    names = Path("../urls").glob("baby*.txt")
    for name in names:
        download_list(name)

    name = Path("../urls/infant.txt")
    download_list(name)
