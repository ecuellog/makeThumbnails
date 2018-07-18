# Make Thumbnails Python Script
Python script to create lightweight thumbnails for images.

## Prerequisite:
ImageMagick needs to be installed.

```sudo apt install imagemagick```

## Instructions:
1. Copy the ```makeThumbnails.py``` file into the parent directory of your project.
2. Run ```python makeThumbnails.py <directory name> <file extension>``` (directory name is relative).  
Example: ```python makeThumbnails.py public/assets/images jpg```
3. Done.
  
A new directory called "thumbnails" will be created in the specified directory with the thumbnail images.
