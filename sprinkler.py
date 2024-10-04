# Import some standard python libraries.
import sys
import time
import pprint as pp
import pickle

# Import a library that comes pre-installed on the RPi.
# It's nonstandard - not part of a standard python installation
# but already downloaded and installed on an RPi.
import gpiozero

import relayRoutines   as rr
import profileRoutines as pr
import timeRoutines    as tr
#############################################################################

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
#############################################################################

# GPIO Number to board pin (and relay num) cross reference dictionary.
# https://pinout.xyz/
gpioDict = { 'GPIO5' : { 'pin': 29, 'relay': 1 },
             'GPIO6' : { 'pin': 31, 'relay': 2 },
             'GPIO13': { 'pin': 33, 'relay': 3 },
             'GPIO16': { 'pin': 36, 'relay': 4 },
             'GPIO19': { 'pin': 35, 'relay': 5 },
             'GPIO20': { 'pin': 38, 'relay': 6 },
             'GPIO21': { 'pin': 40, 'relay': 7 },
             'GPIO26': { 'pin': 37, 'relay': 8 }} 
#############################################################################
 
# Build a list of gpiozero.OutputDevice objects. One obj for each relay.
relay_GPIO_NumLst = [RELAY_1_GPIO, RELAY_2_GPIO, RELAY_3_GPIO, RELAY_4_GPIO,
                     RELAY_5_GPIO, RELAY_6_GPIO, RELAY_7_GPIO, RELAY_8_GPIO]

rlyGPIoObjLst  = []
for relay_GPIO_Num in relay_GPIO_NumLst:
    rlyGPIoObjLst.append( gpiozero.OutputDevice( relay_GPIO_Num, 
                                                      active_high=False, 
                                                      initial_value=False ) )
#############################################################################


if __name__ == "__main__":
    print(' Starting program ...')

    with open('schedDict.pickle', 'rb') as handle:
        profDict = pickle.load(handle)

    strToFunctDict = {
    'or'  : {'func': rr.openRelay,        'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Open    Relay      '},
    'cr'  : {'func': rr.closeRelay,       'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Close   Relay      '},
    'tr'  : {'func': rr.toggleRelay,      'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Toggle  Relay      '},
    'rr'  : {'func': rr.readRelay,        'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Read    Relay      '},
    'cycr': {'func': rr.cycleRelays,      'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Cycle   Relays \n  '},

    'mp'  : {'func': pr.makeProfile,      'parm': None,                              'menu': ' List    Profiles   '},
    'lp'  : {'func': pr.listProfiles,     'parm': profDict,                          'menu': ' List    Profiles   '},
    'gap' : {'func': pr.getActiveProfile, 'parm': profDict,                          'menu': ' Get Act Profile    '},
    'sap' : {'func': pr.setActiveProfile, 'parm': profDict,                          'menu': ' Set Act Profile    '},
    'rap' : {'func': pr.runActiveProfile, 'parm': [rlyGPIoObjLst,gpioDict,profDict], 'menu': ' Run Act Profile \n '},

    'gt'  : {'func': tr.getTimeDate,      'parm': None,                              'menu': ' Get     Time       '},
    }

    while(1):
        choice = input( ' ***** Choice (m=menu, q=quit) -> ' )

        if choice in strToFunctDict:
            function = strToFunctDict[choice]['func']
            params   = strToFunctDict[choice]['parm']
            rtnVal   = function(params)

        elif choice == 'm':
            print()
            for k in strToFunctDict.keys():
                print('{:4} - {}'.format(k, strToFunctDict[k]['menu'] ))
            print()

        elif choice == 'q':
            break

    rtnVal = rr.openRelay([rlyGPIoObjLst,gpioDict,[1,2,3,4,5,6,7,8]])

    print('\n Exiting application. \n')
