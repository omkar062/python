import os
import cv2
import numpy as np

file_name = input("Enter jpg file name: ")
dir_name = os.path.dirname(file_name)
base_name = os.path.basename(file_name)
file_basename = os.path.splitext(base_name)[0]

inp_file = f'{file_name}'

# Open image
img = cv2.imread(inp_file)

print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img1 = cv2.merge([r, g, b])


# Save as planar BGR output file
name1 = f'{dir_name}/{file_basename}-raw-bgr.bin'
# Save as planar RGB output file
name2 = f'{dir_name}/{file_basename}-raw-rgb.bin'

with open(name1, 'w+b') as f:
    f.write(img.copy())
with open(name2, 'w+b') as f:
    f.write(img1.copy())
