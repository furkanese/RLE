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


im_color = cv2.imread('biber.bmp')
im_bw = cv2.imread('res_bw.bmp',0)
im_grayscale = cv2.imread('result_grayscale4.bmp',0)

'''
COLOR
'''
color_b,color_g,color_r = cv2.split(im_color)
(rgb_row, rgb_col) = np.shape(color_b)

# ROW
r_row_encoded = image_codec.encode_image_rowcol(color_r, rgb_row, rgb_col, 'row')
np.savetxt('biber_rgb_encode_r_row.txt', r_row_encoded, fmt='%d',newline=' ')
g_row_encoded = image_codec.encode_image_rowcol(color_g, rgb_row, rgb_col, 'row')
np.savetxt('biber_rgb_encode_g_row.txt', g_row_encoded, fmt='%d',newline=' ')
b_row_encoded = image_codec.encode_image_rowcol(color_b, rgb_row, rgb_col, 'row')
np.savetxt('biber_rgb_encode_b_row.txt', b_row_encoded, fmt='%d',newline=' ')

r_row_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_r_row.txt','row')
g_row_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_g_row.txt','row')
b_row_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_b_row.txt','row')

image_codec.save_as_image_rgb(r_row_decoded,g_row_decoded,b_row_decoded,'biber_rgb_row.bmp')

# COLUMN

r_col_encoded = image_codec.encode_image_rowcol(color_r, rgb_row, rgb_col, 'col')
np.savetxt('biber_rgb_encode_r_col.txt', r_col_encoded, fmt='%d',newline=' ')
g_col_encoded = image_codec.encode_image_rowcol(color_g, rgb_row, rgb_col, 'col')
np.savetxt('biber_rgb_encode_g_col.txt', g_col_encoded, fmt='%d',newline=' ')
b_col_encoded = image_codec.encode_image_rowcol(color_b, rgb_row, rgb_col, 'col')
np.savetxt('biber_rgb_encode_b_col.txt', b_col_encoded, fmt='%d',newline=' ')

r_col_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_r_col.txt','col')
g_col_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_g_col.txt','col')
b_col_decoded = image_codec.decode_image_rowcol('biber_rgb_encode_b_col.txt','col')

image_codec.save_as_image_rgb(r_col_decoded,g_col_decoded,b_col_decoded,'biber_rgb_col.bmp')

'''
GRAY 4 BIT
'''
color_gray = cv2.split(im_grayscale)
(g_channel,g_row, g_col) = np.shape(color_gray)

gray_row_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'row')
np.savetxt('biber_gray_encode_row.txt', gray_row_encoded, fmt='%d',newline=' ')
bw_row_decoded = image_codec.decode_image_rowcol('biber_gray_encode_row.txt','row')
image_codec.save_as_image_gray(bw_row_decoded,'biber_decoded_gray_row.bmp')

gray_col_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'col')
np.savetxt('biber_gray_encode_col.txt', gray_col_encoded, fmt='%d',newline=' ')
bw_col_decoded = image_codec.decode_image_rowcol('biber_gray_encode_col.txt','col')
image_codec.save_as_image_gray(bw_col_decoded,'biber_decoded_gray_col.bmp')

'''
BLACK AND WHITE
'''
# (thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
color_bw = cv2.split(im_bw)
(bw_channel, bw_row, bw_col) = np.shape(color_bw)

bw_row_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'row')
np.savetxt('biber_bw_encode_row.txt', bw_row_encoded, fmt='%d',newline=' ')
bw_row_decoded = image_codec.decode_image_rowcol('biber_bw_encode_row.txt','row')
image_codec.save_as_image_gray(bw_row_decoded,'biber_decoded_bw_row.bmp')

bw_col_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'col')
np.savetxt('biber_bw_encode_col.txt', bw_col_encoded, fmt='%d',newline=' ')
bw_col_decoded = image_codec.decode_image_rowcol('biber_bw_encode_col.txt','col')
image_codec.save_as_image_gray(bw_col_decoded,'biber_decoded_bw_col.bmp')

bw_zig, bw_zig_encoded = image_codec.encode_zigzag(color_bw[0])
np.savetxt('biber_bw_encode_zigzag.txt', bw_zig_encoded, fmt='%d',newline=' ')
bw_zig_decoded = image_codec.decode_zigzag('biber_bw_encode_zigzag.txt')
image_codec.save_as_image_gray(bw_zig_decoded,'biber_decoded_bw_zigzag.bmp')

cv2.imshow('bw', im_bw)
cv2.imshow('image', im_color)
cv2.imshow('im', im_grayscale)
cv2.waitKey(0)
