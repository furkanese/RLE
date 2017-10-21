"""
3 - Black and White
3 - 4 bit grayscale
3 - colored with color table
MFE

"""
from builtins import print

import cv2
import numpy as np
import image_codec


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

# gray_row_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'row')
# np.savetxt('biber_gray_encode_row.txt', gray_row_encoded, fmt='%d',newline=' ')
#
# gray_col_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'col')
# np.savetxt('biber_gray_encode_col.txt', gray_col_encoded, fmt='%d',newline=' ')

'''
BLACK AND WHITE
'''
# (thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = cv2.imread('res_bw.bmp',0)
color_bw = cv2.split(im_bw)
(bw_channel, bw_row, bw_col) = np.shape(color_bw)

bw_row_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'row')
np.savetxt('biber_bw_encode_row.txt', bw_row_encoded, fmt='%d',newline=' ')
bw_row_decoded = image_codec.decode_image_rowcol('biber_bw_encode_row.txt','row')
image_codec.save_as_image_gray(bw_row_decoded,'biber_decoded_row.bmp')

bw_col_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'col')
np.savetxt('biber_bw_encode_col.txt', bw_col_encoded, fmt='%d',newline=' ')
bw_col_decoded = image_codec.decode_image_rowcol('biber_bw_encode_col.txt','col')
image_codec.save_as_image_gray(bw_col_decoded,'biber_decoded_col.bmp')

# bw_zig, bw_zig_encoded = image_codec.encode_zigzag(color_bw[0])
# np.savetxt('biber_bw_encode_zigzag.txt', bw_zig_encoded, fmt='%d',newline=' ')


cv2.imshow('bw', im_bw)
cv2.imshow('image', im_color)
cv2.imshow('im', im_grayscale)
cv2.waitKey(0)
