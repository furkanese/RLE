from PIL import Image
import numpy as np
import cv2

'''
CONVERSION BLOCK
By Berk Taşkın
'''
col=Image.open('biber.bmp')
# converting to 7 bit grayscale and saving
gray_scale = col.convert("L")
gray_scale.save('result_grayscale7.bmp')
# on a seperate object converting and saving 16 color grayscale
gray_scale4 = gray_scale.point(lambda x: int(x / 17) * 17)
gray_scale4.save('result_grayscale4.bmp')
# conversion and saving of BW image
im_grayscale = cv2.imread('biber.bmp',0)
(thresh, im_bw) = cv2.threshold(im_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite('res_bw.bmp',im_bw)

'''
Pixel By Pixel encoding
'''
color_space= cv2.imread('biber.bmp')
b,g,r = cv2.split(color_space)