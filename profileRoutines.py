import pprint        as pp
import datetime      as dt
import relayRoutines as rr
import timeRoutines  as tr
import pickle
import time
import yaml

def makeProfile( prmLst ):
    with open('config.yml', 'r') as file:
        schedDict = yaml.safe_load(file)
    
    with open('schedDict.pickle', 'wb') as handle:
        pickle.dump(schedDict, handle)
    
    with open('schedDict.pickle', 'rb') as handle:
        sd = pickle.load(handle)
    
    pp.pprint(sd)

    return 0
#############################################################################

def listProfiles( pDict ):
    print()
    for profile,sched in pDict.items():
        print('',profile)
        for theKey,data in sched.items():
            print('  ', theKey, end = '')
            if theKey.startswith('relay'):
                print('  Days: {}, Times: {}, Durations: {}'.\
                    format(data['Days'], data['Times'], data['durations']))
            else:
                print(' ',data)
        print()
#############################################################################

def getActiveProfile( pDict ):

    ap = None

    for profileKey,profileValue in pDict.items():
        for profKey,profValue in profileValue.items():
            if profKey == 'active':
                if profValue:
                    ap = profileKey
                    break
        if ap != None:
            break

    print(' Active Profile = {}'.format(ap))

    return ap
#############################################################################

def setActiveProfile( pDict ):

    ap = input(' Active Profile -> ')

    for profileKey,profileValue in pDict.items():
        for profKey,profValue in profileValue.items():
            if profKey == 'active':
                if profileKey == ap:
                    pDict[profileKey]['active'] = True
                else:
                    pDict[profileKey]['active'] = False

    return pDict
#############################################################################

def runActiveProfile( parmLst ):

    relay_ObjLst = parmLst[0] # For access to relay methods.
    gpioDic      = parmLst[1] # For print Statements (pin, gpio, .. )
    pDict        = parmLst[2] # profile dict
    rtnVal = 0
    dowStrLst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    apName = getActiveProfile( pDict )
    apDict = pDict[apName]
    print(' Running Profile')

    try:
        while 1:

            currDT = tr.getTimeDate(None, False)

            for relay,data in apDict.items():
                if relay == 'active':
                    continue
                relayNum = int(relay[-1])
                onDays    = data['Days']
                onTimes   = data['Times']
                durations = data['durations'] 
                print(relay, onDays, onTimes, durations)

                dayMatch = False
                if 'all' in onDays                        or \
                'even' in onDays and currDT['day']%2 == 0 or \
                'odd'  in onDays and currDT['day']%2 == 1 or \
                currDT['dowStr'] in onDays:
                    dayMatch = True
                print( ' day match  = ', dayMatch)

                inOnWindow = False
                if dayMatch:
                    for t,d in zip(onTimes,durations):
                        onTime = dt.datetime(
                            currDT['year'], currDT['month'], currDT['day'], 
                            t//100, t%100, 0)
                        offTime = onTime + dt.timedelta(seconds = d*60)
                        print(' onTime     = ', onTime)
                        print(' now        = ', currDT['now'])
                        print(' offTime    = ', offTime)

                        if onTime <= currDT['now'] <= offTime:
                            inOnWindow = True
                print(' inOnWindow = ', inOnWindow)

                if inOnWindow:
                    relayState = rr.readRelay([relay_ObjLst,gpioDic,[relayNum]])
                    if relayState == 'open':
                        rtnVal = rr.closeRelay([relay_ObjLst,gpioDic,[relayNum]] )
                else:
                    relayState = rr.readRelay([relay_ObjLst,gpioDic,[relayNum]])
                    if relayState == 'closed':
                        rtnVal = rr.openRelay( [relay_ObjLst,gpioDic,[relayNum]] )
                print()

            time.sleep(2)

    except KeyboardInterrupt:
        return rtnVal
#############################################################################

