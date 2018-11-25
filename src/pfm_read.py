#############################
##
## pfm_read.py
## This script provide the method to read the .pfm data.
##
##
#############################
import numpy as np
import re
import sys
from struct import *
from matplotlib import pyplot as plt


def read_pfm(file):
    """

    :param file: Pfald des PFM Datei
    :return:
    img:
    width:
    height:
    """
    with open(file, "rb") as f:
        # Line 1: PF=>RGB (3 channels), Pf=>Greyscale (1 channel)
        type = f.readline().decode('latin-1')
        if "PF" in type:
            channels = 3
        elif "Pf" in type:
            channels = 1
        else:
            sys.exit(1)
        # Line 2: width height
        line = f.readline().decode('latin-1')
        width, height = re.findall('\d+', line)
        width = int(width)
        height = int(height)

        # Line 3: +ve number means big endian, negative means little endian
        line = f.readline().decode('latin-1')
        BigEndian = True
        if "-" in line:
            BigEndian = False
        # Slurp all binary data
        samples = width * height * channels;
        buffer = f.read(samples * 4)
        # Unpack floats with appropriate endianness
        if BigEndian:
            fmt = ">"
        else:
            fmt = "<"
        fmt = fmt + str(samples) + "f"
        img = unpack(fmt, buffer)
    return img, height, width

path = ''#Path of data
offset = 6.095237853035104
depth_img, height, width = read_pfm(path)
depth_img = np.array(depth_img)
depths = 24*100/(depth_img+offset)
depths = np.reshape(depth_img, (height, width))
depths = np.fliplr([depths])[0]
fig = plt.figure('Pfm')
plt.imshow(depths)
plt.colorbar()
fig.savefig(path +'/Pfm_Read.png', dpi=fig.dpi)

