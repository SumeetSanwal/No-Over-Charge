import psutil
from tkinter import *
from tkinter import simpledialog,messagebox
import time

while(1):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        root=Tk()
        root.withdraw()
        pc=simpledialog.askinteger("PERCENTAGE", "ENTER PERCENTAGE FOR NOTIFICATION")
        while(percent<pc and plugged):
            battery = psutil.sensors_battery()
            percent=battery.percent
            plugged = battery.power_plugged
            time.sleep(30)

        while(percent>=pc and plugged):
            battery = psutil.sensors_battery()
            percent = battery.percent
            plugged = battery.power_plugged
            x='Battery is at '+str(percent)+'%'
            messagebox.showinfo("Battery Monitor",x)
            time.sleep(300)
            battery = psutil.sensors_battery()
            percent = battery.percent
            plugged = battery.power_plugged


    else:
        time.sleep(30)

