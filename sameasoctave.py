#!/usr/bin/python

import cv2
import numpy as np

image = np.eye(32)
image = 255*image

for t in range(1,100) :
    s = "python-%03d.bmp" %t
    m = np.arange(0,32) + t * np.arange(0,32)[:,None]
    p = np.exp(-2*np.pi*1j/32 * m)
    im = np.real(np.fft.ifft2(np.multiply(np.fft.fft2(image),p)))
    cv2.imwrite(s,im)


