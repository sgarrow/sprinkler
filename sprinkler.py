# Import some standard python libraries.
import sys
import time
import datetime
import inspect
import pprint as pp
import pickle

# Import a library that comes pre-installed on the RPi.
# It's nonstandard - not part of a standard python installation
# but already downloaded and installed on an RPi.
import gpiozero
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

relay_GPIOS_ObjLst  = []
for relay_GPIO_Num in relay_GPIO_NumLst:
    relay_GPIOS_ObjLst.append( gpiozero.OutputDevice( relay_GPIO_Num, 
                                                      active_high=False, 
                                                      initial_value=False ) )
#############################################################################

def relayOCT( parmLst ): # Relay Open/Close/Toggle

    relay_ObjLst = parmLst[0]
    gpioDic      = parmLst[1]
    relayObjIdxs = parmLst[2]


    if relayObjIdxs == None:
        myLegalStrLst = ['1','2','3','4','5','6','7','8']
        relayObjIdxs  = ['0']
        while not all( el in myLegalStrLst for el in relayObjIdxs ):
            relayObjIdxs = input(' relays -> ').split()
            print(relayObjIdxs)
    relays = [ relay_ObjLst[int(el)-1] for el in relayObjIdxs ]

    whoCalledMeFuncNameStr = inspect.stack()[1][3]
    for relay in relays:
        gpioStr  = str(relay.pin)
        pinNum   = gpioDic[gpioStr]['pin'] 
        relayNum = gpioDic[gpioStr]['relay']
    
        if whoCalledMeFuncNameStr == 'openRelay':
            print(' Opening relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
            relay.off()
        if whoCalledMeFuncNameStr == 'closeRelay':
            print(' Closing relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
            relay.on()
        if whoCalledMeFuncNameStr == 'toggleRelay':
            print(' Toggling relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
            relay.toggle()
    return 0
#############################################################################

def openRelay( parmLst ):
    relayOCT( parmLst )
    return 0
#############################################################################

def closeRelay( parmLst ):
    relayOCT( parmLst )
    return 0
#############################################################################

def toggleRelay( parmLst ):
    relayOCT( parmLst )
    return 0
#############################################################################

def cycleRelays( parmLst ):

    relay_ObjLst = parmLst[0]
    gpioDic      = parmLst[1]

    try:
        while(1):
            for relay in relay_ObjLst:
        
                gpioStr  = str(relay.pin)
                pinNum   = gpioDic[gpioStr]['pin'] 
                relayNum = gpioDic[gpioStr]['relay']
            
                print(' Closing relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
                relay.on()
                time.sleep(1)
                print(' Opening relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
                relay.off()
                time.sleep(1)

    except KeyboardInterrupt:
        pass
    return 0
#############################################################################
def listProfiles( profileDict ):
    print()
    for profile,sched in profileDict.items():
        print('',profile)
        for relay,data in sched.items():
            print('  ', relay)
            print('     Days: {}, Times: {}, Durations: {}'.\
                format(data['Days'], data['Times'], data['durations']))
        print()
#############################################################################
def getActiveProfile( ap ):
    print(' Active Profile = {}'.format(ap))
    return ap
def setActiveProfile( ap ):
    ap = input(' Active Profile -> ')
    return ap
def runActiveProfile( ap ):
    print(' Active Profile = {}'.format(ap))
    return ap
#############################################################################

def getTimeDate( parmLst ):
    now = datetime.datetime.now()
    pp.pprint(now)

    year   = now.year  
    month  = now.month 
    day    = now.day   
    hour   = now.hour  
    minute = now.minute
    second = now.second
    dow    = now.weekday() # Monday is 0.

    print('year   {:4}'.format( year   ))
    print('month  {:4}'.format( month  ))
    print('day    {:4}'.format( day    ))
    print('hour   {:4}'.format( hour   ))
    print('minute {:4}'.format( minute ))
    print('second {:4}'.format( second ))
    print('dow    {:4}'.format( dow    ))

    return year,month,day,hour,minute,second,dow
#############################################################################

if __name__ == "__main__":
    print(' Starting program ...')

    with open('schedDict.pickle', 'rb') as handle:
        profileDict = pickle.load(handle)
    activeProfile = None

    strToFunctDict = {
    'or'  : {'func': openRelay,        'parm': [relay_GPIOS_ObjLst,gpioDict,None], 'menu': ' Open   Relay       '},
    'cr'  : {'func': closeRelay,       'parm': [relay_GPIOS_ObjLst,gpioDict,None], 'menu': ' Close  Relay       '},
    'tr'  : {'func': toggleRelay,      'parm': [relay_GPIOS_ObjLst,gpioDict,None], 'menu': ' Toggle Relay       '},
    'cycr': {'func': cycleRelays,      'parm': [relay_GPIOS_ObjLst,gpioDict,None], 'menu': ' Cycle  Relays      '},

    'gt'  : {'func': getTimeDate,      'parm': None,                               'menu': ' Get    Time        '},

    'lp'  : {'func': listProfiles,     'parm': profileDict,                        'menu': ' List   Profiles    '},
    'gap' : {'func': getActiveProfile, 'parm': activeProfile,                      'menu': ' Get Active Profile '},
    'sap' : {'func': setActiveProfile, 'parm': activeProfile,                      'menu': ' Set Active Profile '},
    'rap' : {'func': runActiveProfile, 'parm': activeProfile,                      'menu': ' Run Active Profile '},
    }

    while(1):
        choice = input( ' ***** Choice (m=menu, q=quit) -> ' )

        if choice in strToFunctDict:
            function= strToFunctDict[choice]['func']
            params  = strToFunctDict[choice]['parm']
            rtnVal  = function(params)
            if choice == 'sap':
                strToFunctDict['gap']['parm'] = rtnVal
                strToFunctDict['sap']['parm'] = rtnVal
                strToFunctDict['rap']['parm'] = rtnVal

            #print(rtnVal)

        elif choice == 'm':
            print()
            for k in strToFunctDict.keys():
                print('{:4} - {}'.format(k, strToFunctDict[k]['menu'] ))
            print()

        elif choice == 'q':
            break

    openRelay([relay_GPIOS_ObjLst,gpioDict,[1,2,3,4,5,6,7,8]])

    print('\n Exiting application. \n')
