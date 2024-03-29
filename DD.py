"""
    --------------------- AKDR ---------------------
    
    This Code is Used to Drive/Display the  0.96" OLED Display

"""
import machine as MAC
from ssd1306 import SSD1306_I2C
import framebuf
import time

# Logo Buffer Section
LogoBuff = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xfc\x00\x00\x00\x00\x00\x000\x1c\x00\x00\x00\x00\x00\x000>\x00\x00\x00\x00\x00\x00`6\x00\x00\x00\x00\x00\x00`c\x00\x00\x00\x00\x00\x00\xc0c\x00\x00\x00\x00\x00\x01\xc0\xc1\x80\x00\x00\x00\x00\x01\x81\xc1\x80\x00\x00\x00\x00\x01\x81\x80\xc0\x00\x00\x00\x00\x03\x03\x80\xe0\x00\x00\x00\x00\x07\x03\x00`\x00\x00\x00\x00\x06\x07\x00p\x00\x00\x00\x00\x0e\x06\x100\x00\x00\x00\x00\x0c\x0c8\x18\x00\x00\x00\x00\x18\x0c8\x18\x00\x00\x00\x00\x18\x1c<\x1c\x00\x00\x00\x008\x18n\x0c\x00\x00\x00\x0000\xe6\x06\x00\x00\x00\x00`p\xc7\x07\x00\x00\x00\x00\xe0a\xc3\x03\x00\x00\x00\x00\xc0a\x83\x83\x00\x00\x00\x01\xc0\xc3\xc1\x81\x80\x00\x00\x01\x81\xc3\xc0\xc1\xc0\x00\x00\x03\x01\x86`\xc0\xc0\x00\x00\x03\x03\x86p`\xe0\x00\x00\x07\x03\xff\xf0``\x00\x00\x06\x07\xff\xf800\x00\x00\x0c\x00\x00888\x00\x00\x1c\x00\x00\x1c\x18\x18\x00\x00\x18\x00\x00\x0c\x1c\x1c\x00\x008\x00\x00\x0e\x0c\x0c\x00\x000\x00\x00\x06\x0e\x0e\x00\x00p?\xff\xff\x06\x06\x00\x00`\x7f\xff\xff\x03\x07\x00\x00\xe0x\x00\x00\x03\x03\x00\x00\xc0\xd8\x00\x00\x01\x81\x80\x01\x80\xdc\x00\x00\x01\x81\x80\x01\x81\xcc\x00\x00\x00\xc1\xc0\x03\xff\x86\x00\x00\x00\xc0\xe0\x03\xff\x86\xff\xff\x80`\xc0\x01\x81\x87\xff\xff\xc0q\xc0\x01\xc0\xc7\xff\xff\xc01\x80\x00\xc0\xce\x00\x00`;\x80\x00\xe0l\x00\x00`\x1b\x00\x00`8\x00\x000\x0e\x00\x00\x7f\xf8\x00\x00?\xfe\x00\x00?\xf0\x00\x00\x1f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Copyright Buffer Section
CopyRBF = bytearray(b'\x00\x00\x00\x1f\xfc\x00\x00\x00\x00\x00\x01\xff\xff\xc0\x00\x00\x00\x00\x1f\xff\xff\xf0\x00\x00\x00\x00\x7f\xff\xff\xfc\x00\x00\x00\x01\xff\xff\xff\xff\x80\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x0f\xff\xff\xff\xff\xf0\x00\x00/\xff\xff\xff\xff\xf8\x00\x00?\xff\xc0\x03\xff\xfc\x00\x00\x7f\xfe\x00\x00\xff\xfe\x00\x00\xff\xf8\x00\x00\x1f\xff\x00\x01\xff\xe0\x00\x00\x07\xff\x00\x03\xff\x80\x00\x00\x03\xff\xc0\x03\xff\x80\x00\x00\x01\xff\xc0\x07\xfe\x00\x00\x00\x00\x7f\xe0\x0f\xfc\x00\x00\x00\x00?\xf0\x0f\xfc\x00\x87\xf0\x00?\xf0\x1f\xf8\x00\x7f\xfe\x00\x1f\xf0\x1f\xf0\x01\xff\xff\x00\x0f\xf8?\xe0\x03\xff\xff\xc0\x07\xfc?\xe0\x07\xff\xff\xe8\x07\xfc?\xc0\x0f\xff\xff\xf0\x03\xfc?\xc0\x1f\xff\xff\xf0\x03\xfc\x7f\x80?\xff\xff\xf0\x03\xfe\x7f\x81?\xf8\x1f\xf0\x01\xfe\x7f\x80\x7f\xe0\x07\xf0\x01\xfe\x7f\x80\x7f\xc0\x07\xa0\x00\xff\xff\x00\x7f\x80\x00\x00\x00\xff\xff\x00\x7f\x80\x00\x00\x00\xfb\xff\x00\xff\x00\x00\x00\x00\xff\xff\x00\xff\x00\x00\x02\x00\xff\xff\x00\xff\x00\x02\x00\x00\xff\xff\x00\xff\x00\x00\x00\x00\xff\xff\x00\xff\x00\x00\x00\x00\xff\xff\x00\xff\x00\x00\x00\x00\xff\xff\x00\x7f\x80\x00\x00\x00\xff\xff\x00\x7f\x80\x00\x08\x00\xff\x7f\x00\x7f\xc0\x03\xe0\x00\xff\x7f\x80\x7f\xe0\x07\xf0\x01\xfe\x7f\x80?\xfc?\xf0\x01\xfe\x7f\xc8\x1f\xff\xff\xf0\x03\xfe?\xc0\x1f\xff\xff\xf0\x07\xfc?\xc0\x0f\xff\xff\xf0\x03\xfc?\xe0\x06\xff\xff\xe0\x07\xfc?\xf0\x03\xff\xff\xc0\x0f\xf8\x1f\xf0\x00\xff\xff\x00\x0f\xf8\x0f\xd8\x00\x7f\xfc\x00\x1f\xf0\x0f\xfc\x00\x00\x80\x00\x7f\xf0\x0f\xfc\x00\x00\x00\x00\x7f\xe0\x07\xfe\x00\x00\x00\x00\x7f\xe0\x03\xff\x80\x00\x01\x01\xff\xc0\x03\xff\xc0\x00\x00\x03\xff@\x00\xff\xe0\x00\x00\x0f\xff\x00\x00\xff\xf8\x00\x00\x1f\xff\x00\x04?\xff\x00\x80\xff\xfe\x00\x00?\xff\xc0\x07\xff\xfc\x00\x00\x0e\xff\xff\xff\xff\xe0\x00\x00\x0f\xff\xff\xff\xff\xe0\x00\x00\x03\xff\xff\xff\xff\xc0\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00?\xff\xff\xfc\x00\x00\x00\x00\x1f\xff\xff\xf0\x00\x00\x00\x00\x01\xff\xff\x00\x00\x00\x00\x00\x00_\xf8\x00\x00\x00')


# Initialize Logo Frame Buffer with Logo Resolution and Color Mode - MONO CHROME
Logo = framebuf.FrameBuffer(LogoBuff, 64, 64, framebuf.MONO_HLSB)

# Initialize Copyright Frame Buffer with Copyright Resolution and Color Mode - MONO CHROME
CopyR = framebuf.FrameBuffer(CopyRBF, 64, 64, framebuf.MONO_HLSB)

# Width and Height of the Display
W = 128 ; H = 64

# Defining the I2C Pins in the Machine With SoftI2C in the machine Module
I2C = MAC.SoftI2C(scl=MAC.Pin(22), sda=MAC.Pin(21))

# Defining the Width, Height and I2C to the SSD1306_I2C 
D = SSD1306_I2C(W, H, I2C)

# The Below func is Used to Test the 0.96" oled Display
def Test_FUNC():
    
    D.fill(0) ; D.text("This is a Test", 0, 0) ; D.show()
    D.text("Message for", 1, 10); D.show()
    D.text("Displaying this", 1, 20) ; D.show()
    D.text("Message from", 1, 30) ; D.show()
    D.text("Display Driver", 1, 40) ; D.show()
    D.text("Function..", 1, 50) ; D.show()

# This Function is used to Display the Data
def Disp(txt, w, h):
    D.fill(0) ; D.text(txt, w, h) ; D.show()

# This Function is used to Display the Logo with The Frame Buffer which is already declared
def Image():
    D.fill(0) ; D.blit(Logo, 32, 0) ; D.show()
    time.sleep(3)
    D.fill(0) ; D.text("AKDR", 50, 20); D.text("CORPORATION", 25, 30) ; D.show()
    time.sleep(3)
    D.fill(0) ; D.blit(CopyR, 32, 0) ; D.show() ; time.sleep(3)