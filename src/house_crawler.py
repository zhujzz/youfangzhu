# -*- coding: utf-8 -*-
"""
@author: zhujz
@file: house_crawler.py
@time: 2018/3/16-16:56
"""
import os

import PIL.ImageOps
import logging
import pytesseract
from PIL import Image

LOG = logging.getLogger()


def convert_verification_code(image_path):
    """

    :param image_path:
    :return:
    """
    def init_table(threshold=140):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table

    try:
        if not os.path.exists(image_path):
            return ''
        im = Image.open(image_path)
        im = im.convert('L')
        binary_image = im.point(init_table(), '1')
        im1 = binary_image.convert('L')
        im2 = PIL.ImageOps.invert(im1)
        im3 = im2.convert('1')
        im4 = im3.convert('L')
        im4.show()
        asd = pytesseract.image_to_string(im4)
        return asd
    except Exception as e:
        LOG.exception('convert_verification_code error: %s' % e)
        return ''
