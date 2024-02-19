#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import time


from PIL import Image

from lib_waveshare_epd import epd2in13b_V4

epd = epd2in13b_V4.EPD()

screenWidth = epd.height
#screenWidth = 250
screenHeight = epd.width
#screenHeight = 122

def clear_screen():
    """
    Clear the screen
    """
    #logging.info("Goto Sleep...")
    epd.init()
    epd.Clear()
    time.sleep(2)
    epd.sleep()
    
    #logging.info("init and Clear")
    #epd.init()
    #epd.Clear(0xFF)



def draw_image_on_hardware(img: Image):
    """
    Draw given image to hardware e-ink
    Does not close img
    :param img: Image
    """
    #img.show()
    epd.init()

    #black image
    img.save(os.path.join("/tmp", "image.png"))
    
    #blank redimage
    redimage = Image.new('1', (epd.height, epd.width), 255)  # 250*122

    #black image file
    screen_output_file = Image.open(os.path.join("/tmp", "image.png"))
    #epd.display(epd.getbuffer(screen_output_file))

    #first draw makes black image, second draw overlays red image (must to draw twice on BWR display), drawing the same image twice will result a red image
    epd.display(epd.getbuffer(screen_output_file), epd.getbuffer(redimage))

    #logging.info("Goto Sleep...")
    time.sleep(2)
    epd.sleep()


