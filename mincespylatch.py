from gpiozero import *
from time import sleep
import socket

pie = GPIODevice(21)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This IP will need to be the IP of your external Pi Zero.
sock.connect(('IP HERE', 9050)) # Connect to remote server

data = ''
hes_been = False

try:
    while True:
        # Check to see if he's been, and the Mince Pie has moved.
        if (pie.value == True and hes_been == False):
            # If the pie has moved, and he's not been previously, let's tell the world he's been!
            data = 'True'.encode()
            print('Santa has been!')
            hes_been = True
            # Also,tell our remote Alert Pi that he's been.
            sock.sendall(data)
        elif(hes_been):
            # If he's been, we need to check that the mince pie hasn't been replaced.
            if(pie.value == False):
                # If the mince pie has been replaced, let's reset everything.
                data = 'False'.encode()
                print('Mince Pie Reset.')
                # Also tell our remote Alert Pi to turn off the lights.
                sock.sendall(data)
                hes_been = False
        sleep(1)

except KeyboardInterrupt:
    pie.close()
