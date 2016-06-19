#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
from lxml import html
import time
import string
import random

# Configuration
FILEFORMAT = ".gif"     # checked file format
RSSFILE = "rss.txt"      # file with rss urls"
TIMEOUT = 10            # timeout second before check new url
FILE_PATH = "gifs/"
HOME_DIR = "./"
LINEFILENAME = 16       # use for len name file
SYMBOLS = string.ascii_uppercase + string.digits + string.ascii_uppercase.lower()
END = len(SYMBOLS)

# TODO Add loging and try statements
# TODO Last post date/time to file

class Gif:
    gif_url = ""
    gif_path = ""
    md5_hash = 0

    def get_gif(self, file_path):
        pass

    def calculate_hash(self):
        #TODO if md5_hash is empty to create hash for this file
        pass

    def move_file(self, file, destination):
        #TODO move file to the new directory
        pass

def get_rss_xml(rss_url):
    # Get xml from url

    # TODO Add try catch return errors
    rss_xml = urllib.request.urlopen(rss_url).read()
    return ET.fromstring(rss_xml)

def naming(file_name_len, end):
    #Return randomize name for file
    file_name = ""
    for i in range(0, file_name_len, 1):
        file_name += SYMBOLS[random.randrange(0, end, 1)]
    return file_name

def get_gifs(rss):
    # Get gifs link from xml

    gifs = []
    for child in rss[0]:
        if child.tag == 'item':
            description = child.find('description')
            if description is not None:
                tree = html.fromstring(description.text)
                images = tree.xpath("//img/@src")
                for i in images:
                    if i[-4:] == FILEFORMAT:
                        l = Gif
                        l.gif_url = i
                        gifs.append(l)
    return gifs

if __name__ == "__main__":
    try:
        with open(RSSFILE) as rss_file:
            for url in rss_file:
                try:
                    rss = get_rss_xml(url)
                    gifs = get_gifs(rss)
                    if gifs != []:
                        pass

                    print("sleep one second")
                    time.sleep(1)
                except:
                    print("Error: work url %s" % url)

            # TODO create function with check return of get_gifs answer

    except:
        print("ERROR cannot open the file %s" % RSSFILE)
        exit(1)