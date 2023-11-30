# This Library is used to import and use System Functions only! 
import machine as MAC

Sens0 = MAC.Pin(0, MAC.Pin.IN)
Sens1 = MAC.Pin(2, MAC.Pin.IN)


#TestPinVCC = MAC.Pin(15, MAC.Pin.OUT)
#TestPinVCC.on()

def reboot():
    MAC.reset()
    
def sensorData():
    print("\nSensor 0: ",Sens0.value())
    print("\nSensor 1: ",Sens1.value())