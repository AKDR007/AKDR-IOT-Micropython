# MACHINE Functions Like Read Sensor Value, Machine Reset After System Update etc., 
#import MACF, time

# Network Function Defined in Below imported Lib
import Network

# Required Package Installation has been Defined in Below imported Lib
import Installer

# Display Function Defined in Below Lib
import DD

# Updater Lib to update the Firmware in this device with Github data
import Updater

DD.Image()

# The Below Line Connectes to your WiFi Network
Network.CON_NW()

# Uncomment the Below Line to Install the required Packages from the imported Lib
# Installer.Ins()

# Uncomment the Below Line to Test the OLED Screen ( 0.96" )
# DD.Test_FUNC()


# Updater.samp_res()

# DD.Disp(Network.IPADDR())

"""while True:
    print("\n")
    MACF.sensorData()
    time.sleep(2)"""