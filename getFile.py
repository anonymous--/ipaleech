#import re
#import sites
links = {'appaddict', 'iphonecake'}
from pprint import pprint
#from sites import iphonecake

class getFile(object):

    def __init__(self, shareLink):
        self.shareLink = shareLink

    def checkShare(self):
        site = self.shareLink.split('www.')[1].split('.')[0]
        mod = ('sites.' + site)
        subMod = site
        api = (site + '.getLinks')
        myMod = __import__(mod, fromlist=[subMod, site])
        try:
            return myMod.getApp(self.shareLink).getLinks()
        except:
            pass

#testing = getFile('https://www.iphonecake.com/app_357828853_.html')
testing = getFile('https://www.iphonecake.com/app_479516143_.html')
#print(testing.checkShare())

pprint(testing.checkShare())