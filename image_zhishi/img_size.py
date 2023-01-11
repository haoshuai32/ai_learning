
import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image

file_path = "/Users/haoshuai/Desktop/Unknown.png"

# f_size = os.path.getsize(file_path)
# print(f_size)

img = Image.open(file_path)
print(img.size)
print(img.format)
print(img)

image = cv2.imread(file_path)
print(image.shape)

plt.imshow(image)
plt.show()