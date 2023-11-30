
import network as NW
from NW_CONFIG import SSID, NKEY
import time, DD, MACF

# Common Timing 
COMM_T = 2

WLAN = NW.WLAN(NW.STA_IF)

def CON_NW():
    
    if not WLAN.active():
        DD.Disp("WIFI TURNING ON", 0, 0) ; time.sleep(COMM_T)
    
    WLAN.active(True)
    
    if WLAN.active():
        DD.Disp("Waiting to ", 0, 0) ; time.sleep(COMM_T)
        DD.Disp("Connect..", 0, 0) ; time.sleep(COMM_T)
        
    
    # Debug Purpose:
        #time.sleep(5)
        #print(WLAN.active())
    
    WLAN.connect(SSID, NKEY)
    time.sleep(5)
    
    if not WLAN.isconnected():
        DD.Disp("Error Connecting to", 0, 0) ; time.sleep(COMM_T)
        DD.Disp("WIFI", 0, 0) ; time.sleep(COMM_T)
        DD.Disp("Restarting Sys.", 0, 0) ; time.sleep(COMM_T) ; MACF.reboot()
        
    else:
        DD.Disp("Connected to: ", 0, 0) ; time.sleep(3) ; DD.Disp(SSID, 0, 0)
        time.sleep(COMM_T)
        DD.Disp(("IP: "+IPADDR()), 0, 0)
        
    """
    Below Lines for Debug Purpose:
        
    print(WLAN.isconnected())
    print(WLAN.ifconfig())
    time.sleep(5)
    
    """

def IPADDR():
    IP = WLAN.ifconfig()
    IP = list(IP)[0] 
    return str(IP)