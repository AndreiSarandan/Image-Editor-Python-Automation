from PIL import Image, ImageFilter
import os
import sys


path = str(input('Please input path...'))
path += '\\'
dirs = os.listdir(path)
newpath = path+'resized'+'\\'  # resized folder path
print(newpath)


def resize():
    for image in dirs:
        name = image.split('.')[0]  # get the name of the image
        if os.path.isfile(path+image):
            img = Image.open(path+image)
            f, e = os.path.splitext(path+image)  # file, extension
            imgResize = img.resize((800, 800))
            # add blur effect to image
            imBlur = imgResize.filter(ImageFilter.BLUR)
            # save image in a separate folder
            imBlur.save(f'{newpath}\\{name}_resized.{e}', quality=90)


def make_folder():
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # create new folder


make_folder()
resize()
