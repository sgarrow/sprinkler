import calendar
from datetime import datetime
import yaml
import pprint as pp
import pickle

with open('config.yml', 'r') as file:
    schedDict = yaml.safe_load(file)

with open('schedDict.pickle', 'wb') as handle:
    pickle.dump(schedDict, handle)

with open('schedDict.pickle', 'rb') as handle:
    sd = pickle.load(handle)

#pp.pprint(sd)

print(len(sd))
for profile,sched in sd.items():
    print('',profile)
    for relay,data in sched.items():
        print('  ', relay)
        print('     Days: {}, Times: {}, Durations: {}'.\
            format(data['Days'], data['Times'], data['durations']))
    print()





