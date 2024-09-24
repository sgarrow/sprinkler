import sys
import time
import gpiozero

RELAY_1_PIN = 5  # GPIO 5
RELAY_2_PIN = 6  # GPIO 6
RELAY_3_PIN = 13 # etc.
RELAY_4_PIN = 16
RELAY_5_PIN = 19
RELAY_6_PIN = 20
RELAY_7_PIN = 21
RELAY_8_PIN = 26

gpioDict = { 'GPIO5' : { 'pin': 29, 'relay': 1 },
             'GPIO6' : { 'pin': 31, 'relay': 2 },
             'GPIO13': { 'pin': 33, 'relay': 3 },
             'GPIO16': { 'pin': 36, 'relay': 4 },
             'GPIO19': { 'pin': 35, 'relay': 5 },
             'GPIO20': { 'pin': 38, 'relay': 6 },
             'GPIO21': { 'pin': 40, 'relay': 7 },
             'GPIO26': { 'pin': 37, 'relay': 8 }} 
 
relayPins = [ RELAY_1_PIN, RELAY_2_PIN, RELAY_3_PIN, RELAY_4_PIN,
              RELAY_5_PIN, RELAY_6_PIN, RELAY_7_PIN, RELAY_8_PIN ]

relayLst  = []
for pin in relayPins:
    relayLst.append( gpiozero.OutputDevice( pin, 
                                            active_high=False, 
                                            initial_value=False ) )
#############################################################################

def set_relay(relay, status):
    gpioStr  = str(relay.pin)
    pinNum   = gpioDict[gpioStr]['pin'] 
    relayNum = gpioDict[gpioStr]['relay']
    if status:
        print(' Closing relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
        relay.on()
    else:
        print(' Opening relay {} ({:6} on pin {}).'.format(relayNum, gpioStr, pinNum))
        relay.off()
#############################################################################

def toggle_relay(relay):
    print(' Toggling relay {}'.format(gpioToRelayNumDict[relay.pin]))
    relay.toggle()
#############################################################################

def main_loop():
    # start by turning all the relays off
    for relay in relayLst:
        set_relay(relay, False)
    idx = 0
    while 1:
        relay = relayLst[idx]

        set_relay(relay, True)
        time.sleep(.75)

        set_relay(relay, False)
        time.sleep(.75)

        idx += 1
        if idx == len(relayLst):
            idx = 0
#############################################################################
    
if __name__ == "__main__":
    print(' Starting program ...')

    import datetime

    # Get the current date and time
    now = datetime.datetime.now()
    
    # Extract the desired components
    month = now.strftime("%B")  # Full month name
    day = now.day
    year = now.year
    day_of_week = now.strftime("%A")  # Full weekday name
    ttime = now.strftime("%H:%M:%S")  # Time in HH:MM:SS format
    
    # Print the results
    print('      Month: {}'.format( month       ))
    print('        Day: {}'.format( day         ))
    print('       Year: {}'.format( year        ))
    print('Day of Week: {}'.format( day_of_week ))
    print('       Time: {}'.format( ttime        ))

    try:
        main_loop()
    except KeyboardInterrupt:
        for relay in relayLst:
            set_relay(relay,False)
        print('\n Exiting application. \n')
        sys.exit(0)
