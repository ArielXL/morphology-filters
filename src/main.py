import cv2
import numpy as np
from image import Image

def main():

    kernel = np.ones((7,7), np.uint8)

    # erosion
    image = Image.load_image('../img/lake.tif')
    image_erosion = cv2.erode(image, kernel)
    Image.show_images([ image, image_erosion ])
    Image.plt_show()

    # dilatacion
    image = Image.load_image('../img/living_room.tif')
    image_dilatation = cv2.dilate(image, kernel, iterations=1)
    Image.show_images([ image, image_dilatation ])
    Image.plt_show()

    # apertura
    image = Image.load_image('../img/pirate.tif')
    image_aperture = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    Image.show_images([ image, image_aperture ])
    Image.plt_show()

    # cierre
    image = Image.load_image('../img/peppers.tif')
    image_shutdown = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    Image.show_images([ image, image_shutdown ])
    Image.plt_show()

    # gradiente
    image = Image.load_image('../img/house.tif')
    image_gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    Image.show_images([ image, image_gradient ])
    Image.plt_show()

    # transformacion top-hat
    image = Image.load_image('../img/lena.tif')
    image_top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    Image.show_images([ image, image_top_hat ])
    Image.plt_show()

if __name__ == '__main__':
    main()
