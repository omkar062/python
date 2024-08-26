import os
import cv2
import numpy as np

file_name = input("Enter jpg file name: ")
#base_name = os.path.basename(file_name)
#file_name = os.path.splitext(base_name)[0]

inp_file = f'{file_name}'

# Open image and resize to 512x512
img = cv2.imread(inp_file)

img[:, :, (0, 2)] = 0

# Display resized image
cv2.imshow('Resized Image', img)
if cv2.waitKey(0) == 10:
    cv2.destroyAllWindows()

