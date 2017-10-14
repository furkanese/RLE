'''
3 - Black and White
3 - 4 bit grayscale
3 - 7 bit grayscale
3 - colored with color table
MFE

'''
from builtins import print

import cv2
import numpy as np

def encode_colors(pixels,rows,columns):
    colors = []
    prev_color = 255  # first color taken as white
    cntr = 1
    for i in range(0, rows):
        # we are looping through the image
        if i % 2 == 0:
            for j in range(0, columns):
                if not (i==j==0): # we do not control the first pixel of image
                    next_color = pixels[0][i][j]
                    if next_color == prev_color:
                        cntr += 1
                    else:
                        colors.append(cntr)
                        colors.append(prev_color)
                        prev_color = next_color
                        cntr = 1
        else:
            for j in range(columns - 1, 0, -1):
                if not (i==j==0): # we do not control the first pixel of image
                    next_color = pixels[0][i][j]
                    if next_color == prev_color:
                        cntr += 1
                    else:
                        colors.append(cntr)
                        colors.append(prev_color)
                        prev_color = next_color
                        cntr = 1
    return colors

'''
COLOR
'''
im_color = cv2.imread('pepper.jpg')
color_b,color_g,color_r = cv2.split(im_color)
print(np.shape(color_b))

'''
GRAY 4 BIT
'''
im_grayscale = cv2.imread('pepper.jpg',0)
color_gray = cv2.split(im_grayscale)
(g_channel,g_row, g_col) = np.shape(color_gray)
# gray_encoded = encode_colors(color_gray,g_row,g_col)
# print(np.shape(gray_encoded))

'''
GRAY 7 BIT
'''


'''
BLACK AND WHITE
'''
(thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
color_bw = cv2.split(im_bw)
(bw_channel,bw_row, bw_col) = np.shape(color_bw)
bw_encoded = encode_colors(color_bw,bw_row,bw_col)
cv2.imshow('bw',im_bw)

cv2.imshow('image',im_color)
cv2.imshow('im',im_grayscale)
cv2.waitKey(0)
