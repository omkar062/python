import os
import cv2
import numpy as np

file_name = input("Enter raw image file: ")
base_name = os.path.basename(file_name)
dir_name = os.path.dirname(file_name)
file_basename_noext = os.path.splitext(base_name)[0]

inp_file = f'{file_name}'

# Open image
fd = open(inp_file, 'rb')
rows = int(input("Enter Hight of the raw image: "))
cols = int(input("Enter Width of the raw image: "))
channels = 3
f = np.fromfile(fd, dtype=np.uint8,count=rows*cols*channels)
print(f.size)

im = f.reshape((rows, cols, channels)) #notice row, column format
print(im)
fd.close()

# Display resized image
cv2.imshow(inp_file, im)
if cv2.waitKey(0) == 5:
    cv2.destroyAllWindows()
