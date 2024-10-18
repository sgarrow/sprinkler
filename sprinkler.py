''' 
This is the main script for the sprinkler project.
To run it from the RPi command line type "python3 sprinkler.py".
This project (collection of files/scripts) cannot be run on a PC, 
it has to be run on an RPi.

Every file in this project has comments like this at the top.
Comments like this (enclosed by three single quotes) are called doc-strings.
doc-strings are like comments but ... different. Comments are proceeded by #.

The recommended way to learn about this project is to read the comments at 
the top of the files in this order:
  initRoutines.py, timeRoutines.py, relayRoutines.py, 
  profileRoutines.py, config.yml.

After reading the doc-strings perusing the comments will also be helpful.
'''

# Import a standard python libraries.
import pickle

# Import other source files that are in the same directory as this file.
import initRoutines    as ir
import timeRoutines    as tr
import relayRoutines   as rr
import profileRoutines as pr
import utilRoutines    as ur
#############################################################################

if __name__ == "__main__":

    print(' Starting program ...\n')
    ur.getVer(None)
    ur.getTemp(None)

    gpioDict, rlyGPIoObjLst = ir.init()

    with open('schedDict.pickle', 'rb') as handle:
        profDict = pickle.load(handle)

    strToFunctDict = {
    'or'  : {'func': rr.openRelay,        'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Open    Relay      '},
    'cr'  : {'func': rr.closeRelay,       'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Close   Relay      '},
    'tr'  : {'func': rr.toggleRelay,      'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Toggle  Relay      '},
    'rr'  : {'func': rr.readRelay,        'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Read    Relay      '},
    'cycr': {'func': rr.cycleRelays,      'parm': [rlyGPIoObjLst,gpioDict,None],     'menu': ' Cycle   Relays \n  '},

    'mp'  : {'func': pr.makeProfile,      'parm': None,                              'menu': ' Make    Profiles   '},
    'lp'  : {'func': pr.listProfiles,     'parm': profDict,                          'menu': ' List    Profiles   '},
    'gap' : {'func': pr.getActiveProfile, 'parm': profDict,                          'menu': ' Get Act Profile    '},
    'sap' : {'func': pr.setActiveProfile, 'parm': profDict,                          'menu': ' Set Act Profile    '},
    'rap' : {'func': pr.runActiveProfile, 'parm': [rlyGPIoObjLst,gpioDict,profDict], 'menu': ' Run Act Profile \n '},

    'gdt' : {'func': tr.getTimeDate,      'parm': None,                              'menu': ' Get     Date/Time  '},
    'gt'  : {'func': ur.getTemp,          'parm': None,                              'menu': ' Get     CPU Temp   '},
    'gv'  : {'func': ur.getVer,           'parm': None,                              'menu': ' Get     Version    '},
    }

    while(1):
        inputStr = input( '\n ***** Choice (m=menu, q=quit) -> ' )

        if inputStr == '': continue

        inputWords = inputStr.split()
        choice     = inputWords[0]
        optArgsStr = inputWords[1:]
        optArgs    = [ int(x) for x in optArgsStr ]

        print( 'inputStr   = ', inputStr   )
        print( 'inputWords = ', inputWords )
        print( 'choice     = ', choice     )
        print( 'optArgs    = ', optArgs    )

        if choice in strToFunctDict:
            function = strToFunctDict[choice]['func']
            params   = strToFunctDict[choice]['parm']
            if choice in ['or','cr','rr','cycr'] and len(optArgs) > 0:
                params[2] = optArgs

            rtnVal   = function(params)

        elif choice == 'm':
            print()
            for k in strToFunctDict.keys():
                print('{:4} - {}'.format(k, strToFunctDict[k]['menu'] ))

        elif choice == 'q':
            break

    rtnVal = rr.openRelay([rlyGPIoObjLst,gpioDict,[1,2,3,4,5,6,7,8]])

    print('\n Exiting application. \n')
