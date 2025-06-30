# Load image1.png and image2.png.
# Reduce the resolution by a factor of 5

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images in colour
img1 = cv2.imread('image1.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('image2.png', cv2.IMREAD_COLOR)

# Resize the images
img1 = cv2.resize(img1, (0,0), fx=0.5, fy=0.5)
img2 = cv2.resize(img2, (0,0), fx=0.5, fy=0.5)


# Save the images as image1.png and image2.png
cv2.imwrite('image1.png', img1)
cv2.imwrite('image2.png', img2)
