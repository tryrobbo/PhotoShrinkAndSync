__author__ = 'thomas'

from functools import partial
from PIL import Image
import hashlib

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def ShrinkAndSave(SourceFilePath,maxsize,DestinationFilePath):
    im = Image.open(SourceFilePath)
    size = (maxsize, maxsize)
    im.thumbnail(size, Image.LANCZOS)
    im.show()
    im.save(DestinationFilePath)
    return md5sum(SourceFilePath)
