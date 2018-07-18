import os
import sys

if len(sys.argv) < 3:
    print "Please run this script in the following form:"
    print "python makeThumbnails.py <DIRECTORY> <FILE EXTENSION>"
    print "For example: python makeThumbnails.py images jpg"
    sys.exit()

targetDir = sys.argv[1]
fileExt = sys.argv[2]

os.system("mkdir " + targetDir + "/thumbnails") 
for file in os.listdir(targetDir):
    if file.endswith("." + sys.argv[2]):
        os.system("convert " + targetDir + "/" + file + " -resize 400 -quality 80 " + targetDir + "/thumbnails/"+ file)
        print targetDir + "/" + file + " -resize 400 -quality 80 " + targetDir + "/thumbnails/"+ file
