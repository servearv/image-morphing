"""
Write a python program that
1. Loads two images, img1.png and img2.png
2. Resizes them to the maximum common size
3. Saves the resized images as image1.png and image2.png
"""

import cv2

img1 = cv2.imread('./Outputs/kitty4.jpg')
img2 = cv2.imread('./Outputs/kitty3.jpg')

# Resize the images
height1, width1, _ = img1.shape
height2, width2, _ = img2.shape

if height1 > height2:
    img1 = cv2.resize(img1, (width1 * height2 // height1, height2))
    img2 = cv2.resize(img2, (width1 * height2 // height1, height2))
else:
    img1 = cv2.resize(img1, (width2 * height1 // height2, height1))
    img2 = cv2.resize(img2, (width2 * height1 // height2, height1))

# Save the images
cv2.imwrite('image1.png', img1)
cv2.imwrite('image2.png', img2)

