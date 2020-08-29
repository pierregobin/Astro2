#!/usr/bin/python

import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename",help="prefix of files",default="image")
parser.add_argument("-n","--number", type=int, help="number of images",default=1)
parser.add_argument( "--height", type=int, help="height of images", default=256)
parser.add_argument( "--width", type=int, help="width of images", default=256)
parser.add_argument("--drifth", type=int, help="image drift", default=0)
parser.add_argument("--driftv", type=int, help="image drift", default=0)
parser.add_argument("--noise_mean", type=int, help="mean noise", default=0)
parser.add_argument("--noise_sigma", type=float, help="sigma noise", default=0.0)
parser.add_argument("--suffix",help="image format",default="bmp")
args=parser.parse_args()
filename=args.filename
number_of_image=args.number+1
drifth=args.drifth
driftv=args.driftv
noise_mean=args.noise_mean
noise_sigma=args.noise_sigma
suffix=args.suffix


black_image = np.zeros((256,256,1),np.uint8)
for i in range(1,number_of_image):
    b1 = np.copy(black_image)
    noise=np.random.normal(noise_mean,noise_sigma,(b1.shape[0],b1.shape[1],b1.shape[2]))
    cv2.circle(b1,(100+i*drifth,100+i*driftv),10,(255,0,0),3)
    s = "org-%s-%05d.bmp" %(filename, i)
    cv2.imwrite(s,b1)
    b1 = b1 + noise
    b1 = b1.astype(int)
    s = "%s-%05d.%s" %(filename, i, suffix)
    cv2.imwrite(s,b1)



