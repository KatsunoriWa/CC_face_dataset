#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import urllib.request
from pathlib import Path

from download_images import download_list

if __name__ == "__main__":
    name = Path("../ncc_urls/ncc_elder2.txt")
    download_list(name)
