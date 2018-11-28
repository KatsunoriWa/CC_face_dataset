#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import urllib.request
from pathlib import Path

name = "../urls/urls.txt"

imageDir = Path("../imageDir")
imageDir.mkdir(exist_ok=True)

for line in open(name, "rt"):
    if line.find("https") >-1:
        url = line.strip()
        basename = os.path.basename(url)
        urllib.request.urlretrieve(url,"{0}".format(str(imageDir))+"/"+basename)
