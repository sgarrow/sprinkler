import inspect
import time

def relayOCTR( parmLst ): # Relay Open/Close/Toggle/Read Driver Function.

    relay_ObjLst = parmLst[0]
    gpioDic      = parmLst[1]
    relayObjIdxs = parmLst[2]
    rtnVal = None

    if relayObjIdxs == None:
        myLegalStrLst = ['1','2','3','4','5','6','7','8']
        relayObjIdxs  = ['0']
        while not all( el in myLegalStrLst for el in relayObjIdxs ):
            relayObjIdxs = input(' relays -> ').split()
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
            
                rtnVal = closeRelay( [relay_ObjLst,  gpioDic, [ii+1]])
                time.sleep(1)
                rtnVal = openRelay( [relay_ObjLst,  gpioDic, [ii+1]])
                time.sleep(1)

    except KeyboardInterrupt:
        pass
    return rtnVal
#############################################################################

