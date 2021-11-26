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
import requests
import ftplib
import xml.etree.ElementTree as ET
import textwrap

logging.basicConfig(level=logging.DEBUG)
    
try:

    logging.info("Blackheath weather started")

    # initialise the epaper
    epd = epd3in7.EPD()
    logging.info("init and Clear")
    epd.init(0)
    epd.Clear(0xff, 0)

    # set some variables
    # import some data from the BOM
    x = requests.get("http://www.bom.gov.au/fwo/IDN60801/IDN60801.94743.json", headers={'User-Agent': 'My User Agent 1.0'})
    jsonData = x.json()
    temp = jsonData["observations"]["data"][0]["air_temp"]
    feelsLike = jsonData["observations"]["data"][0]["apparent_t"]
    lastChecked = jsonData["observations"]["data"][0]["local_date_time"]

    # get forecast data from ftp and parse the xml
    FTP_host = "ftp.bom.gov.au"
    FTP = ftplib.FTP()
    FTP.connect(FTP_host)
    FTP.login()
    FTP.cwd("/anon/gen/fwo/") # navigate to correct directory
    FTP.retrbinary("RETR IDN11109.xml", open('myxml.xml', 'wb').write)

    minTemp = '-'
    maxTemp = '-'
    forecast = '-'
    root = ET.parse('myxml.xml').getroot()
    latestElement = root[1][1][0]
    dataElements = latestElement.findall('element')
    dataTexts = latestElement.findall('text')
 
    for dataElement in dataElements:
        if(dataElement.get('type') == 'air_temperature_minimum'):
            minTemp = dataElement.text
        if(dataElement.get('type') == 'air_temperature_maximum'):
            maxTemp = dataElement.text
        
    for dataText in dataTexts:
        if(dataText.get('type') == 'forecast'):
            forecasts = textwrap.wrap(dataText.text, width=30)
        
    font60 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 60)
    font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    Rimage = Image.new('L', (epd.width, epd.height), 0xFF)
    draw = ImageDraw.Draw(Rimage)

    # place the weather elements
    draw.rectangle((0, 0, 300, 89), fill=0)
    draw.text((30, 30), 'Blackheath Weather', font = font24, fill = epd.GRAY1)
    #draw.line((0, 90, 300, 90), fill = 0)
    #draw.line((0, 400, 300, 400), fill = 0)

    draw.text((10, 110), "min", font=font18, fill=epd.GRAY3)
    draw.text((10, 130), minTemp+"°", font=font24, fill=epd.GRAY4)
    draw.text((100, 110), "max", font=font18, fill=epd.GRAY3)
    draw.text((100, 130), maxTemp+"°", font=font24, fill=epd.GRAY4)
        
    draw.text((10, 175), "Current temp", font=font18, fill=epd.GRAY3)
    draw.text((10, 190), str(temp)+"°", font=font60, fill=epd.GRAY4)
        
    draw.text((10, 265), "Feels like", font=font18, fill=epd.GRAY3)
    draw.text((10, 290), str(feelsLike)+"°", font=font24, fill=epd.GRAY4)

    draw.text((10, 320), "Last checked: "+lastChecked, font=font18, fill=epd.GRAY4)
        
    top = 340
    for forecast in forecasts:
        draw.text((10, top), forecast, font=font18, fill=epd.GRAY4)
        top += 20
        

    epd.display_1Gray(epd.getbuffer(Rimage))
    time.sleep(1)
        
    logging.info("Goto Sleep...")
    epd.sleep()
    #time.sleep(1800) # 30 minutes
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in7.epdconfig.module_exit()
    exit()
