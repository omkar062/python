import cv2
import os

import numpy as np

file_name = input("Enter jpg file name: ")
dir_name = os.path.dirname(file_name)
base_name = os.path.basename(file_name)
file_basename = os.path.splitext(base_name)[0]


inp_file = file_name

H = int(input("Enter hight to resize: "))
W = int(input("Enter width to resize: "))

# Read input image
img = cv2.imread(inp_file)

# Specify desired output size
output_size = (H, W)

# Resize image
resized_img = cv2.resize(img, output_size, interpolation=cv2.INTER_AREA)

out_file = f'{dir_name}/{file_basename}-{H}x{W}.jpg'
# Write the resized image to a file
cv2.imwrite(out_file, resized_img)
