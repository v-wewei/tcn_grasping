#!/usr/bin/env python3

from PIL import Image
from data import H, W
import argparse
import math
import os

# show a collage of a point in time across all cameras

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--img-dir', type=str, default='imgs', help='root dir for imgs')
parser.add_argument('--run', type=int, default=1, help='which run to show')
parser.add_argument('--frame', type=int, default=0, help='which frame to show')
opts = parser.parse_args()

# collect all imgs for run / frame
imgs = []
for camera_dir in os.listdir(opts.img_dir):
    fname = "%s/%s/r%02d/f%03d.png" % (opts.img_dir, camera_dir, opts.run, opts.frame)
    print("fname", fname)
    imgs.append(Image.open(fname))

num_cols = 4
num_rows = (len(imgs) // num_cols) +1

collage = Image.new('RGB', (W*num_cols, H*num_rows), (0,0,0))
for i, img in enumerate(imgs):
    col, row = i % num_cols, i // num_cols
    collage.paste(img, (W*col, H*row))
collage.show()
