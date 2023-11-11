import psutil
import sys
import time
from datetime import datetime
import textwrap

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


# Returns system wide Usages
cpuUsage = psutil.cpu_percent(interval=1)
diskUsage = psutil.disk_usage('/')
memoryUsage = psutil.virtual_memory()
Sensors = psutil.sensors_temperatures(fahrenheit= 0)

cpuusagestring = str(cpuUsage)
diskusagestring = str(diskUsage)
memoryusagestring = str(memoryUsage)
sensorsstring = str(Sensors)



while True:
    sys.stdout = open("Usage.txt", "a")
    print("-------------"+ dt_string + "-------------")
    print(" Cpu Usage = " + cpuusagestring)
    print(" Disk Usage = " + diskusagestring)
    print(" Memory Usage = " + memoryusagestring)
    print(" Temperatures = " + sensorsstring)
    print("---------------------------------------------")
    time.sleep(1800)


