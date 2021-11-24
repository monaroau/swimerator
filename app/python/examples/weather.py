#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd3in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import random

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Swimerator started")
    
    # initialise the epaper
    epd = epd3in7.EPD()
    logging.info("init and Clear")
    epd.init(0)
    epd.Clear(0xff, 0)

    # set some variables
    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    Rimage = Image.new('L', (epd.width, epd.height), 0xFF)
    draw = ImageDraw.Draw(Rimage)

    # place the weather elements
    # draw.text((2, 0), 'Blackheath Weather', font = font24, fill = 0)
    # draw.text((2, 200), "weather here", font = font18, fill = 0)


    draw.rectangle((130, 20, 274, 56), 'black', 'black')
    draw.text((130, 20), u'微雪电子', font = font36, fill = epd.GRAY1)
    draw.text((130, 60), u'微雪电子', font = font36, fill = epd.GRAY2)
    draw.text((130, 100), u'微雪电子', font = font36, fill = epd.GRAY3)
    draw.text((130, 140), u'微雪电子', font = font36, fill = epd.GRAY4)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)

    
    epd.display_1Gray(epd.getbuffer(Rimage))
    time.sleep(5)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in7.epdconfig.module_exit()
    exit()
