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
    
    # initialise the epaper and clear the display
    epd = epd3in7.EPD()
    logging.info("init and Clear")
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
