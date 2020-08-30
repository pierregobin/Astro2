#!/usr/bin/python 

import cv2
import numpy as np
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--image",help="image to translate")
parser.add_argument("--output",help="filename of the result")
parser.add_argument("-x",type=float,help="x translation",default=0.)
parser.add_argument("-y",type=float,help="x translation",default=0.)
args=parser.parse_args()
image=args.image
output=args.output
translation_x=args.x
translation_y=args.y

print "translation (%f,%f)" %(translation_x, translation_y)
input_image=cv2.imread(image)
print "input image shape : %d,%d,%d"  %(input_image.shape)
m = translation_x * np.arange(0,input_image.shape[0]) + translation_y * np.arange(0,input_image.shape[1])[:,None]
p = np.exp(2*np.pi*1j / input_image.shape[0] * m)
print "phase shape : %d,%d" %( p.shape)
im = np.zeros(input_image.shape)
im[:,:,0] = np.real(np.fft.ifft2(np.multiply(np.fft.fft2(input_image[:,:,0]),p)))
im[:,:,1] = np.real(np.fft.ifft2(np.multiply(np.fft.fft2(input_image[:,:,1]),p)))
im[:,:,2] = np.real(np.fft.ifft2(np.multiply(np.fft.fft2(input_image[:,:,2]),p)))
print "im shape : %d,%d,%d" %(im.shape)
cv2.imwrite(output,im)
