__author__ = 'thomas'


import PSDefs


SourceFilePath = "/mnt/1TBDrive/Documents and Settings/Thomas/Pictures/12-14-2011_002.jpg"
maxsize = 500
DestinationFilePath="Thumbnail.jpg"


hash = PSDefs.ShrinkAndSave(SourceFilePath,maxsize,DestinationFilePath)
print(hash)
