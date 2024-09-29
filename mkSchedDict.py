import calendar
from datetime import datetime
import yaml
import pprint as pp
import pickle

def create_calendar(year, month):
    """Creates a calendar for the given year and month."""

    # Get the calendar object
    cal = calendar.monthcalendar(year, month)

    # Print the header
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    # Print the calendar
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2}", end=" ")
        print()
    print()

# Get current year and month
now   = datetime.now()
year  = now.year
month = now.month

#print(now  )
#print(year )
#print(month)
#
## Create the calendar
#for month in range(1,13):
#    create_calendar(year, month)

with open('config.yml', 'r') as file:
    schedDict = yaml.safe_load(file)

pp.pprint(schedDict)

with open('schedDict.pickle', 'wb') as handle:
    pickle.dump(schedDict, handle)

with open('schedDict.pickle', 'rb') as handle:
    sd = pickle.load(handle)

pp.pprint(schedDict)



