import os
import cv2
import numpy as np

file_name = input("Enter jpg file name: ")
dir_name = os.path.dirname(file_name)
base_name = os.path.basename(file_name)
file_basename = os.path.splitext(base_name)[0]

inp_file = file_name

# Open image and resize to 512x512
img = cv2.imread(inp_file)
print(img.size)
print(img.dtype)

# Save as planar RGB output file
name = f'{dir_name}/{file_basename}-raw-R_G_B.bin'
raw_image = np.array(img, dtype=np.uint8)

with open(name, 'w+b') as f:
    f.write(img[...,2].copy())     # write Red channel
    f.write(img[...,1].copy())     # write Green channel
    f.write(img[...,0].copy())     # write Blue channel

