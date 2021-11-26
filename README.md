# The swimerator 3000
This project runs on a raspberry pi with an attached epaper display

## Setup
Install the following dependencies
```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
```

## How to run
From the root of the project
```
python ./app/python/examples/runit.py
```

## Crontab
The weather.py example is running on crontab. To view
```
crontab -e
```

## Based on
This repository is based on https://github.com/waveshare/e-Paper

## Raspberry Pi
The Raspberry Pi zero 2 w was used for this project

## e-Paper  
3.7 inch epaper display from waveshare electronics

## English:  
Jetson Nano、Raspberry Pi、Arduino、STM32 Demo:  
* RaspberryPi_JetsonNano:  
    > C
    > Python
* Arduino:  
    > Arduino UNO  
* STM32:  
    > STM32F103ZET6 
    
For more information, please search on the official website:   
https://www.waveshare.com



