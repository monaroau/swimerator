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

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd3in7 Demo")
    
    epd = epd3in7.EPD()
    logging.info("init and Clear")
    epd.init(0)
    epd.Clear(0xff, 0)

    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    strokes = ['backstroke', 'freestyle', 'breaststroke', 'butterfly', 'pulls', 'kicks', 'dives']
    offset = 50
    Rimage = Image.new('L', (epd.width, epd.height), 0xFF)
    draw = ImageDraw.Draw(Rimage)
    draw.text((2, 0), 'the Swimerator 3000', font = font24, fill = 0)
    for stroke in strokes:
        draw.text((2, offset), stroke, font = font18, fill = 0)
        offset += 25
    epd.display_1Gray(epd.getbuffer(Rimage))
    time.sleep(5)

   
            
    logging.info("Clear...")
    epd.init(0)
    epd.Clear(0xff, 0)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in7.epdconfig.module_exit()
    exit()
