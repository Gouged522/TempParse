import logging
import psutil
import sys
import time
import textwrap
from distutils.debug import DEBUG
import datetime
import logging

def LOGGINGINIT():

    
    logging.basicConfig (filename= 'Output.log', encoding='utf-8', level=logging.DEBUG)
    
    LOGEVENTS_INFO(f"Logging started")
    

def LOGEVENTS_INFO(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.info(f"{currentdateandtimestr} " + input)


LOGGINGINIT()

while True:
    # Returns system wide Usages
    cpuUsage = psutil.cpu_percent(interval=1)
    diskUsage = psutil.disk_usage('/')
    memoryUsage = psutil.virtual_memory()
    Sensors = psutil.sensors_temperatures(fahrenheit= 0)

    cpuusagestring = str(cpuUsage)
    diskusagestring = str(diskUsage)
    memoryusagestring = str(memoryUsage)
    sensorsstring = str(Sensors)

    LOGEVENTS_INFO(f"CPU Usage: " + cpuusagestring)
    LOGEVENTS_INFO(f"Disk Usage: " + diskusagestring)
    LOGEVENTS_INFO(f"Memory Usage: " + memoryusagestring)
    LOGEVENTS_INFO(f"Temperatures: " + sensorsstring)
    time.sleep(60)

