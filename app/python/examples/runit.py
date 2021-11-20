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
    Yoffset = 50
    TotalDistance = 3000
    distances = [25, 50, 75, 100, 150, 200, 400, 500, 800, 1000, 1500]
    strokes = ['IM', 'freestyle', 'backstroke', 'breaststroke', 'butterfly', 'kick', 'pull', 'dives', 'turns']
    strokesWithNoDistance = ['dives', 'turns']
    Rimage = Image.new('L', (epd.width, epd.height), 0xFF)
    draw = ImageDraw.Draw(Rimage)

    # generate the swims and render 
    draw.text((2, 0), 'the Swimerator 3000', font = font24, fill = 0)
    i = 0
    while i < TotalDistance:
        randomDistance = distances[random.randint(0, len(distances))-1]
        randomStroke = strokes[random.randint(0, len(strokes))-1]
        if randomStroke in strokesWithNoDistance :
            randomDistance = 0
            randomDistanceString = ''
        else :
            randomDistanceString = str(randomDistance) + "m - "
        i += randomDistance
        draw.text((2, Yoffset), randomDistanceString + randomStroke, font = font18, fill = 0)
        Yoffset += 25
    
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
