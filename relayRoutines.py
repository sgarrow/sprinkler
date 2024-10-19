'''
This module contains all the functions that talk directly to the relays.
This is the only module that talks directly to the relays.

This module has 6 functions 5 of which are callable directly from the prompt.
Commands or,cr,tr,rr,cycr call functions openRelay, closeRelay, toggleRelay
and readRelay, respectively.

The 6th function (relayOCTR) is a driver for or,cr,tr,rr.  Those 4 functions
(openRelay, closeRelay, toggleRelay, readRelay) are just thin wrappers to 
relayOCTR.
'''

import inspect
import time
import utilRoutines as ur

def relayOCTR( parmLst ): # Relay Open/Close/Toggle/Read Driver Function.

    relay_ObjLst = parmLst[0] # This was created by function in file init.py
    gpioDic      = parmLst[1] # Also from init.py, refer to comments therein.
    relayObjIdxs = parmLst[2] # A list of relays to perform the action on.
    rtnVal = None

    if relayObjIdxs == None:  # If the passed in list is empty, prompt user.
        relayObjIdxs = []
        while relayObjIdxs == []:
            relayStr = input(' relays -> ').split()
            relayObjIdxs = ur.verifyRelayArgs( relayStr )

    relays = [ relay_ObjLst[el-1] for el in relayObjIdxs ]
    
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
        if whoCalledMeFuncNameStr == 'readRelay':
            rtnVal = 'open'
            rv = relay.value
            if rv == 1:
                rtnVal = 'closed'
            print(' Reading relay {} ({:6} on pin {}) is {}.'.format(relayNum, gpioStr, pinNum, rtnVal))
    return rtnVal
#############################################################################

def openRelay( parmLst ):   # Wrapper function.
    rtnVal = relayOCTR( parmLst )
    return rtnVal
#############################################################################

def closeRelay( parmLst ):  # Wrapper function. 
    rtnVal = relayOCTR( parmLst )
    return rtnVal
#############################################################################

def toggleRelay( parmLst ): # Wrapper function. 
    rtnVal = relayOCTR( parmLst )
    return rtnVal
#############################################################################

def readRelay( parmLst ):   # Wrapper function. 
    rtnVal = relayOCTR( parmLst )
    return rtnVal
#############################################################################

def cycleRelays( parmLst ):

    relay_ObjLst = parmLst[0]
    gpioDic      = parmLst[1]
    rtnVal = 0
    try:
        while(1):
            for ii,relay in enumerate(relay_ObjLst):
        
                gpioStr  = str(relay.pin)
                pinNum   = gpioDic[gpioStr]['pin'] 
                relayNum = gpioDic[gpioStr]['relay']
            
                rtnVal = closeRelay([relay_ObjLst,  gpioDic, [ii+1]])
                time.sleep(3)
                rtnVal = openRelay( [relay_ObjLst,  gpioDic, [ii+1]])
                time.sleep(3)

    except KeyboardInterrupt:
        pass
    return rtnVal
#############################################################################

