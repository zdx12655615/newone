import urllib.request
import socket
import re
import sys
import os

targetDir = r"C:\Users\null\Desktop\pic"


def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos + 1:])
    return t


if __name__ == "__main__":
    hostname = "http://category.dangdang.com/cid4003599.html"
    req = urllib.request.Request(hostname)
    webpage = urllib.request.urlopen(req)
    contentBytes = webpage.read()
    for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):
        print(link)
        urllib.request.urlretrieve(link, destFile(link))