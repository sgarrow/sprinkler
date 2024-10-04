import datetime      as dt

def getTimeDate( parmLst, prnEn = True ):
    now = dt.datetime.now()

    dowStrLst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    year   = now.year  
    month  = now.month 
    day    = now.day   
    hour   = now.hour  
    minute = now.minute
    second = now.second
    dowNum = now.weekday() # Monday is 0.
    dowStr = dowStrLst[dowNum]

    if prnEn:
        print(now)
        print()
        print(' year   {:4}'.format( year   ), end = '')
        print(' month  {:4}'.format( month  ), end = '')
        print(' day    {:4}'.format( day    ))
        print(' hour   {:4}'.format( hour   ), end = '')
        print(' minute {:4}'.format( minute ), end = '')
        print(' second {:4}'.format( second ))
        print(' dow    {:4} ({})'.format( dowNum, dowStr ))
        print()

    rtnDict = {'year':   year,   'month':  month,  'day':   day,
               'hour':   hour,   'minute': minute, 'second':second,
               'dowNum': dowNum, 'dowStr': dowStr,
               'now':    now}


    return rtnDict
#############################################################################
