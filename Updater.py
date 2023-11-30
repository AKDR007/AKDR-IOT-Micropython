# This Lib is used to get any Updates in the files with github files #

import requests
import time

##

url = "https://raw.githubusercontent.com/AKDR007/AKDR-ESP32-Micropython-Updater/main/"

def samp_res():
    
    res = requests.get(url+"AKDR.py")
    time.sleep(2)
    print(res.text)
    with open("AKDR.py", 'w') as W:
        W.write(res.text)
        W.close()