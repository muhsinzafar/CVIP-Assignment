# import required packages
import cv2

# Read image 1
import numpy as np
from matplotlib.pyplot import figure
from skimage import io

# read & handle images
img1 = cv2.imread('cat_1.jpeg')
rI1 = cv2.resize(img1, (300, 200))
# Read image 2
img2 = cv2.imread('cat_2.png')
rI2 = cv2.resize(img2, (300, 200))
# Define alpha and beta
alpha = 0.2
beta = 0.60
# Blend images
final_image = cv2.addWeighted(rI1, alpha, rI2, beta, 0.0)
# change contrast & brightness of image
# Create a dummy image that stores different contrast and brightness
contrastImage = np.zeros(final_image.shape, final_image.dtype)
# Brightness and contrast parameters
contrast = 1.5
bright = 10
# Change the contrast and brightness
for y in range(final_image.shape[0]):
    for x in range(final_image.shape[1]):
        for c in range(final_image.shape[2]):
            contrastImage[y, x, c] = np.clip(contrast * final_image[y, x, c] + bright, 0, 255)
# Show image
cv2.imshow('Image 1', rI1)
cv2.imshow('Image 2', rI2)
cv2.imshow('Blended Image', final_image)
cv2.imshow('Blended & contrast Image', contrastImage)
# save results
io.imsave('results/Image 1.png', rI1)
io.imsave('results/Image 2.png', rI2)
io.imsave('results/Blended Image.png', final_image)
io.imsave('results/Blended & Contrast Image.png', contrastImage)

# exit the with key
cv2.waitKey(0)


