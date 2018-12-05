from gpiozero import *
from time import sleep

pie = GPIODevice(21)

hes_been = False

try:
    while True:
        # Check to see if he's been, and the Mince Pie has moved.
        if (pie.value == True and hes_been == False):
            # If the pie has moved, and he's not been previously, let's tell the world he's been!
            print('Santa has been!')
            hes_been = True
        elif(hes_been):
            # If he's been, we need to check that the mince pie hasn't been replaced.
            if(pie.value == False):
                # If the mince pie has been replaced, let's reset everything.
                print('Mince Pie Reset.')
                hes_been = False
        sleep(1)

except KeyboardInterrupt:
    pie.close()
