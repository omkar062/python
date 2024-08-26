import cv2
import numpy as np

# Output dimensions
H, W = 512, 512

# Open image and resize to 512x512
img = cv2.imread('image.jpg')
img = cv2.resize(img, (H, W))

# Save as planar RGB output file
name = f'f-{H}x{W}.bin'
with open(name, 'w+b') as f:
    f.write(img[...,2].copy())     # write Red channel
    f.write(img[...,1].copy())     # write Green channel
    f.write(img[...,0].copy())     # write Blue channel

