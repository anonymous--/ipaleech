import requests
from bs4 import BeautifulSoup
#from pprint import pprint
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



class getApp(object):

    def __init__(self, appUrl):
        self.appUrl = appUrl

    def soup(self):
        rawData = requests.get(self.appUrl).content
        soup = BeautifulSoup(rawData, 'html5lib')
        return soup;

    def getVersion(self):
        appInfo = self.soup().find_all('dl', attrs={'class': 'ui-app-meta'})
        version = str(appInfo).split('<dt>Version:</dt><dd>')[1].split("<")[0]
        return version;

    def getLinks(self):
        baseUrl = 'https://www.iphonecake.com/'
        appinfo = []
        sopa = self.soup().find_all(attrs={'class':'ui-btn -link'})
        info = str(sopa)
        #.split('<a class="ui-btn -link"')
        for inteli in info:
            if 'daily' in inteli:
                if self.getVersion() in inteli:
                    appinfo.append(inteli.replace(' href="', 'applink=').replace('amp;', '').replace(
                        '" role="button" target="_blank" title="Download From This Filehost">dailyuploads.net Link</a>\xa0<aapplink=report.php?id=',
                        ' waste ').split('waste')[0].replace(' ', '').replace('applink=', baseUrl))
                    #appinfo.append(inteli)
                    return appinfo;

                    #getFile.getFile(appinfo).checkShare()
testing = getApp('https://www.iphonecake.com/app_479516143_.html')
print(testing.getVersion())
print(testing.getLinks())
