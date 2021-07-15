import cv2  # import numpy as np
import numpy as np


def read_image():
    # read the image
    img = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)
    # save the image
    new_image = cv2.imwrite('saved_image.jpg', img)
    # show the image
    cv2.imshow('name_window', img)
    # waiting a touch key to close a window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


# simple blurring filter
def simple_filtering():
    img = read_image()
    img = cv2.resize(img, (0, 0), None, .55, .55)
    # average in the neighborhood 9 x 9
    # convolution matrix with all coefficients identical and their sum equal to 1
    image1 = cv2.blur(img, (9, 9))
    # use the median on a neighborhood 9 x 9
    image2 = cv2.medianBlur(img, 9)
    im_concatenate_horiz = np.concatenate((image1, image2), axis=1)
    cv2.imshow('window', im_concatenate_horiz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gaussian_blur():
    im = read_image()
    # Gaussian filter of size 5 X 5 and standard deviation of 3
    image = cv2.GaussianBlur(im, (5, 5), 3)
    cv2.imshow('gaussian_blur', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_image()
    # simple_filtering()
    # gaussian_blur()
