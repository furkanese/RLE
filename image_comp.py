"""
3 - Black and White
3 - 4 bit grayscale
3 - colored with color table
MFE

"""
from builtins import print

import cv2
import numpy as np


def encode_image(pixels, rows, columns, encode_type):
    '''
    :param pixels: pixels of the image
    :param rows: row size
    :param columns: column size
    :param encode_type: row wise or column wise
    :return: encoded array
    '''
    colors = []
    prev_color = 255  # first color taken as white
    cntr = 1
    if encode_type == 'row':
        outer_index = rows
        inner_index = columns
    else:
        outer_index = columns
        inner_index = rows

    for i in range(0, outer_index):
        # we are looping through the image
        if i % 2 == 0:
            for j in range(0, inner_index):
                if not (i==j==0): # we do not control the first pixel of image
                    if encode_type == 'row':
                        next_color = pixels[i][j]
                    else:
                        next_color = pixels[j][i]

                    if next_color == prev_color:
                        cntr += 1
                    else:
                        colors.append(cntr)
                        colors.append(prev_color)
                        prev_color = next_color
                        cntr = 1
        else:
            for j in range(inner_index - 1, 0, -1):
                if not (i==j==0): # we do not control the first pixel of image
                    if encode_type == 'row':
                        next_color = pixels[i][j]
                    else:
                        next_color = pixels[j][i]

                    if next_color == prev_color:
                        cntr += 1
                    else:
                        colors.append(cntr)
                        colors.append(prev_color)
                        prev_color = next_color
                        cntr = 1
    # we add the last portion manually
    colors.append(cntr+1)
    colors.append(prev_color)

    return colors


'''
COLOR
'''
im_color = cv2.imread('biber.bmp')
color_b,color_g,color_r = cv2.split(im_color)
print(np.shape(color_b))

'''
GRAY 4 BIT
'''
im_grayscale = cv2.imread('result_grayscale4.bmp',0)
color_gray = cv2.split(im_grayscale)
(g_channel,g_row, g_col) = np.shape(color_gray)

gray_row_encoded = encode_image(color_gray[0], g_row, g_col, 'row')
np.savetxt('biber_gray_encode_row.txt', gray_row_encoded, fmt='%d',newline=' ')

gray_col_encoded = encode_image(color_gray[0], g_row, g_col, 'col')
np.savetxt('biber_gray_encode_col.txt', gray_col_encoded, fmt='%d',newline=' ')

'''
BLACK AND WHITE
'''
# (thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = cv2.imread('res_bw.bmp',0)
color_bw = cv2.split(im_bw)
(bw_channel, bw_row, bw_col) = np.shape(color_bw)

bw_row_encoded = encode_image(color_bw[0], bw_row, bw_col, 'row')
np.savetxt('biber_bw_encode_row.txt', bw_row_encoded, fmt='%d',newline=' ')

bw_col_encoded = encode_image(color_bw[0], bw_row, bw_col, 'col')
np.savetxt('biber_bw_encode_col.txt', bw_col_encoded, fmt='%d',newline=' ')

cv2.imshow('bw', im_bw)
cv2.imshow('image', im_color)
cv2.imshow('im', im_grayscale)
cv2.waitKey(0)
