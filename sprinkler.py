# Import a standard python libraries.
import pickle

# Import other source files that are in the same directory as this file.
import initRoutines    as ir
import timeRoutines    as tr
import relayRoutines   as rr
import profileRoutines as pr
#############################################################################

if __name__ == "__main__":

    print(' Starting program ...\n')

    gpioDict, rlyGPIoObjLst = ir.init()

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
