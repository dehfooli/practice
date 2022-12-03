import math
import random
import time

import qrcode
name= input("please enter name: ")
phone= input("please enter phonenum: ")
QR = name + phone
img = qrcode.make(QR)
img.save("webqrcode.png")