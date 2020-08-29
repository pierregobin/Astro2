#!/usr/bin/python 

import cv2
import numpy as np
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--origin",help="origin")
parser.add_argument("--image",help="image")
args=parser.parse_args()
origin=args.origin
images=glob.glob(args.image)
i1=cv2.imread(origin)
i1=cv2.cvtColor(i1,cv2.COLOR_BGR2GRAY)
i1=np.float32(i1)
for f in images:
    i2=cv2.imread(f)
    i2=cv2.cvtColor(i2,cv2.COLOR_BGR2GRAY)
    i2=np.float32(i2)
    print f , cv2.phaseCorrelate(i1,i2)
