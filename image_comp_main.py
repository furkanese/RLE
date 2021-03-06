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
from PIL import Image


col=Image.open('ucak.bmp')
# converting to 7 bit grayscale and saving
gray_scale = col.convert("L")
gray_scale.save('result_grayscale7.bmp')
# on a seperate object converting and saving 16 color grayscale
gray_scale4 = gray_scale.point(lambda x: int(x / 17) * 17)
gray_scale4.save('result_grayscale4.bmp')
# conversion and saving of BW image
im_grayscale = cv2.imread('ucak.bmp',0)
(thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('res_bw.bmp',im_bw)


im_color = cv2.imread('ucak.bmp')
im_bw = cv2.imread('res_bw.bmp',0)
im_grayscale = cv2.imread('result_grayscale4.bmp',0)
encoded_shapes = []
original_shapes = []

'''
COLOR
'''
color_b,color_g,color_r = cv2.split(im_color)
(rgb_row, rgb_col) = np.shape(color_b)

original_shapes.append(rgb_row * rgb_col * 3)

# ROW
r_row_encoded = image_codec.encode_image_rowcol(color_r, rgb_row, rgb_col, 'row')
np.savetxt('ucak/ucak_rgb_encode_r_row.txt', r_row_encoded, fmt='%d',newline=' ')
g_row_encoded = image_codec.encode_image_rowcol(color_g, rgb_row, rgb_col, 'row')
np.savetxt('ucak/ucak_rgb_encode_g_row.txt', g_row_encoded, fmt='%d',newline=' ')
b_row_encoded = image_codec.encode_image_rowcol(color_b, rgb_row, rgb_col, 'row')
np.savetxt('ucak/ucak_rgb_encode_b_row.txt', b_row_encoded, fmt='%d',newline=' ')

encoded_shapes.append(len(b_row_encoded) + len(g_row_encoded) + len(r_row_encoded))

r_row_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_r_row.txt','row')
g_row_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_g_row.txt','row')
b_row_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_b_row.txt','row')

image_codec.save_as_image_rgb(r_row_decoded,g_row_decoded,b_row_decoded,'out/ucak_rgb_row.bmp')

# COLUMN

r_col_encoded = image_codec.encode_image_rowcol(color_r, rgb_row, rgb_col, 'col')
np.savetxt('ucak/ucak_rgb_encode_r_col.txt', r_col_encoded, fmt='%d',newline=' ')
g_col_encoded = image_codec.encode_image_rowcol(color_g, rgb_row, rgb_col, 'col')
np.savetxt('ucak/ucak_rgb_encode_g_col.txt', g_col_encoded, fmt='%d',newline=' ')
b_col_encoded = image_codec.encode_image_rowcol(color_b, rgb_row, rgb_col, 'col')
np.savetxt('ucak/ucak_rgb_encode_b_col.txt', b_col_encoded, fmt='%d',newline=' ')

encoded_shapes.append(len(b_col_encoded) + len(r_col_encoded) + len(g_col_encoded))

r_col_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_r_col.txt','col')
g_col_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_g_col.txt','col')
b_col_decoded = image_codec.decode_image_rowcol('ucak/ucak_rgb_encode_b_col.txt','col')

image_codec.save_as_image_rgb(r_col_decoded,g_col_decoded,b_col_decoded,'out/ucak_rgb_col.bmp')

# ZIG ZAG

r_zig, r_zig_encoded = image_codec.encode_zigzag(color_r)
np.savetxt('ucak/ucak_r_encode_zigzag.txt', r_zig_encoded, fmt='%d',newline=' ')
g_zig, g_zig_encoded = image_codec.encode_zigzag(color_g)
np.savetxt('ucak/ucak_g_encode_zigzag.txt', g_zig_encoded, fmt='%d',newline=' ')
b_zig, b_zig_encoded = image_codec.encode_zigzag(color_b)
np.savetxt('ucak/ucak_b_encode_zigzag.txt', b_zig_encoded, fmt='%d',newline=' ')

encoded_shapes.append(len(b_zig_encoded) + len(g_zig_encoded) + len(r_zig_encoded))


r_zig_decoded = image_codec.decode_zigzag('ucak/ucak_r_encode_zigzag.txt')
g_zig_decoded = image_codec.decode_zigzag('ucak/ucak_g_encode_zigzag.txt')
b_zig_decoded = image_codec.decode_zigzag('ucak/ucak_b_encode_zigzag.txt')

image_codec.save_as_image_rgb(r_zig_decoded,g_zig_decoded,b_zig_decoded,'out/ucak_decoded_rgb_zigzag.bmp')

'''
GRAY 4 BIT
'''
color_gray = cv2.split(im_grayscale)
(g_channel,g_row, g_col) = np.shape(color_gray)
original_shapes.append(g_row * g_col * 1)

gray_row_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'row')
np.savetxt('ucak/ucak_gray_encode_row.txt', gray_row_encoded, fmt='%d',newline=' ')
gray_row_decoded = image_codec.decode_image_rowcol('ucak/ucak_gray_encode_row.txt','row')
image_codec.save_as_image_gray(gray_row_decoded,'out/ucak_decoded_gray_row.bmp')

encoded_shapes.append(len(gray_row_encoded))

gray_col_encoded = image_codec.encode_image_rowcol(color_gray[0], g_row, g_col, 'col')
np.savetxt('ucak/ucak_gray_encode_col.txt', gray_col_encoded, fmt='%d',newline=' ')
bw_col_decoded = image_codec.decode_image_rowcol('ucak/ucak_gray_encode_col.txt','col')
image_codec.save_as_image_gray(bw_col_decoded,'out/ucak_decoded_gray_col.bmp')

encoded_shapes.append(len(gray_col_encoded))


gray_zig, gray_zig_encoded = image_codec.encode_zigzag(color_gray[0])
np.savetxt('ucak/ucak_gray_encode_zigzag.txt', gray_zig_encoded, fmt='%d',newline=' ')
gray_zig_decoded = image_codec.decode_zigzag('ucak/ucak_gray_encode_zigzag.txt')
image_codec.save_as_image_gray(gray_zig_decoded,'out/ucak_decoded_gray_zigzag.bmp')

encoded_shapes.append(len(gray_zig_encoded))


'''
BLACK AND WHITE
'''
# (thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
color_bw = cv2.split(im_bw)
(bw_channel, bw_row, bw_col) = np.shape(color_bw)

original_shapes.append(bw_row * bw_col * 1)

bw_row_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'row')
np.savetxt('ucak/ucak_bw_encode_row.txt', bw_row_encoded, fmt='%d',newline=' ')
bw_row_decoded = image_codec.decode_image_rowcol('ucak/ucak_bw_encode_row.txt','row')
image_codec.save_as_image_gray(bw_row_decoded,'out/ucak_decoded_bw_row.bmp')

encoded_shapes.append(len(bw_row_encoded))

bw_col_encoded = image_codec.encode_image_rowcol(color_bw[0], bw_row, bw_col, 'col')
np.savetxt('ucak/ucak_bw_encode_col.txt', bw_col_encoded, fmt='%d',newline=' ')
bw_col_decoded = image_codec.decode_image_rowcol('ucak/ucak_bw_encode_col.txt','col')
image_codec.save_as_image_gray(bw_col_decoded,'out/ucak_decoded_bw_col.bmp')

encoded_shapes.append(len(bw_col_encoded))

bw_zig, bw_zig_encoded = image_codec.encode_zigzag(color_bw[0])
np.savetxt('ucak/ucak_bw_encode_zigzag.txt', bw_zig_encoded, fmt='%d',newline=' ')
bw_zig_decoded = image_codec.decode_zigzag('ucak/ucak_bw_encode_zigzag.txt')
image_codec.save_as_image_gray(bw_zig_decoded,'out/ucak_decoded_bw_zigzag.bmp')

encoded_shapes.append(len(bw_zig_encoded))

np.savetxt('ucak/ucak_org.txt', original_shapes, fmt='%d')
np.savetxt('ucak/ucak_enc.txt', encoded_shapes, fmt='%d')


cv2.imshow('bw', im_bw)
cv2.imshow('image', im_color)
cv2.imshow('im', im_grayscale)
cv2.waitKey(0)
