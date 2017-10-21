"""
Encode and Decode image
"""
import numpy as np
import scipy


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
                if not (i == 0) & (j == 0): # we do not control the first pixel of image
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
            for j in range(inner_index - 1, -1, -1):
                if not (i == 0) & (j ==0): # we do not control the first pixel of image
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
    colors.append(cntr)
    colors.append(prev_color)
    return colors


def squarify_image(pixels):
    """
    Makes the given array into a square one
    :param pixels:
    :return:
    """
    padded_pixels = pixels.copy()
    print(np.shape(padded_pixels))
    rows, columns = np.shape(padded_pixels)
    sz = np.abs(rows - columns)
    if rows > columns:
        # add new columns to image
        new_col = np.zeros([rows, sz], dtype=int)
        padded_pixels = np.hstack(padded_pixels, new_col)
    else:
        # add new rows to image
        new_row = np.zeros([sz, columns], dtype=int)
        padded_pixels = np.vstack([padded_pixels, new_row])

    print(np.shape(padded_pixels))
    return padded_pixels


def save_as_image_gray(pixels):
    """
    Saves an image with given pixel values
    ONLY BW AND GRAYSCALE
    :param pixels:
    :return:
    """
    rows, columns = np.shape(pixels)
    img = np.zeros((rows, columns, 3), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0,columns):
            img[i][j][0] = pixels[i][j]
            img[i][j][1] = pixels[i][j]
            img[i][j][2] = pixels[i][j]
    scipy.misc.imsave('deneme.bmp', img)


