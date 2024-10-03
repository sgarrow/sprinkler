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

pp.pprint(sd)
