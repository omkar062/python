import os
import cv2
import numpy as np

file_name = input("Enter jpg file name: ")
base_name = os.path.basename(file_name)
file_name = os.path.splitext(base_name)[0]

inp_file = f'{file_name}.jpg'

# Open image and resize to 512x512
img = cv2.imread(inp_file)

print(img.shape)
# (225, 400, 3)

print(img.dtype)
# uint8
img[(1,2), :, :] = 0

print(img)
img[:, :, (0, 1)] = 0

print(img)
# Display resized image
cv2.imshow('Resized Image', img)
if cv2.waitKey(0) == 10:
    cv2.destroyAllWindows()

