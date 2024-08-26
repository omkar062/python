import os
import cv2
import numpy as np

file_name = input("Enter jpg file name: ")
base_name = os.path.basename(file_name)
file_name = os.path.splitext(base_name)[0]

inp_file = f'{file_name}.jpg'

# Open image and resize to 512x512
img = cv2.imread(inp_file)
# Save as scalar RGB output file
tmp_img = img
name1 = f'{file_name}-raw-R.bin'
with open(name1, 'w+b') as f:
    f.write(tmp_img[...,2].copy())     # write Red channel
tmp_img = img
name2 = f'{file_name}-raw-G.bin'
with open(name2, 'w+b') as f:
    f.write(tmp_img[...,1].copy())     # write Green channel
tmp_img = img
name3 = f'{file_name}-raw-B.bin'
with open(name3, 'w+b') as f:
    f.write(tmp_img[...,0].copy())     # write Blue channel

