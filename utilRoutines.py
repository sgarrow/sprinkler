import gpiozero

VERSION  = ' Version:  1.0'
RELEASED = ' Released: 14-Oct-2024'
#############################################################################

def getTemp(prmLst):
    cpu = gpiozero.CPUTemperature()
    print(' CPU Temp  = {}'.format(cpu.temperature))
    print(' Over Temp = {}'.format(cpu.is_active))
    return cpu
#############################################################################

def getVer(prmLst):
    print(VERSION)
    print(RELEASED)
    return VERSION, RELEASED
#############################################################################

