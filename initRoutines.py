'''
Create (1) a list of gpiozero relay-objects and (2) a dictionary of GPIO to
board-pin and associated relay it is wired to. These items are returned.

Relay-objs have methods on,off,pin to close,open,get-GPIO-name, respectively.
The returned dictionary is just used to make the print statements more 
meaningfull, other than that there is no real functionality.
'''

# Import a library that comes pre-installed on the RPi. It's nonstandard - 
# not part of a standard python installation but already downloaded and 
# installed on an RPi. Lots of data on the gpiozero here:
# https://gpiozero.readthedocs.io/en/latest/
import gpiozero

def init():

    # GPIO Number to board pin (and relay num) cross reference dictionary.
    # https://pinout.xyz/ .The data in this dict is only needed/used in 
    # print statements. A given relayObj (there ane 8 such objs in the list
    # (variable) rlyGPIoObjLst, created below) has a "method" named "pin". 
    # So doing something like x = relay.pin will result in x being assigned a
    # value like "GPIO5". From that one can print the  RPi pin number and 
    # associated relay that that pin is controlling.
    gpioDict = { 'GPIO5' : { 'pin': 29, 'relay': 1 },
                 'GPIO6' : { 'pin': 31, 'relay': 2 },
                 'GPIO13': { 'pin': 33, 'relay': 3 },
                 'GPIO16': { 'pin': 36, 'relay': 4 },
                 'GPIO19': { 'pin': 35, 'relay': 5 },
                 'GPIO20': { 'pin': 38, 'relay': 6 },
                 'GPIO21': { 'pin': 40, 'relay': 7 },
                 'GPIO26': { 'pin': 37, 'relay': 8 }} 
    #################################################
     
    # From the relay board datasheet.
    # https://www.waveshare.com/wiki/RPi_Relay_Board_(B)
    RELAY_1_GPIO = 5
    RELAY_2_GPIO = 6
    RELAY_3_GPIO = 13
    RELAY_4_GPIO = 16
    RELAY_5_GPIO = 19
    RELAY_6_GPIO = 20
    RELAY_7_GPIO = 21
    RELAY_8_GPIO = 26
    #################################################

    # A list of nums used in creating (below) a second list - of relay objs.
    relay_GPIO_NumLst = [RELAY_1_GPIO,RELAY_2_GPIO,RELAY_3_GPIO,RELAY_4_GPIO,
                         RELAY_5_GPIO,RELAY_6_GPIO,RELAY_7_GPIO,RELAY_8_GPIO]
    
    # Build a list of gpiozero.OutputDevice objects. One obj for each relay.
    # These are the most important lines of code in project. Refer to:
    # https://johnwargo.com/posts/2017/driving-a-relay-board-from-python-using-gpio-zero/
    # All other gpiozero module docs on-line just talks about LED, Buttons, 
    # but this one shows how to create your own "class" type ... of type "relay".
    rlyGPIoObjLst  = []
    for relay_GPIO_Num in relay_GPIO_NumLst:
        rlyGPIoObjLst.append( gpiozero.OutputDevice( 
            relay_GPIO_Num, 
            active_high   = False, 
            initial_value = False ))
    #################################################
    
    # Ok, after all that return the only two things 
    # that the rest of the system needs.
    return gpioDict, rlyGPIoObjLst

