#from getFile import getFile
#import json
from pprint import pprint
from sites import iphonecake

appList = 'https://www.iphonecake.com/app_357828853_.html'

pprint(iphonecake.getApp(appList).getLinks())