import requests
from bs4 import BeautifulSoup as sopa


class appaddict(object):
    def __init__(self, appUrlLink):
        self.appUrlLink = appUrlLink

    def version(self):
        rawData = requests.get(self.appUrlLink).text
        soup = sopa(rawData, 'html5lib')
        for findVersion in soup.find_all('div', attrs={'class': 'center-stack'}):
            for version in findVersion.find_all('span', attrs={'class': 'aa-app-version'}):
                version = str(version).split('<span class="aa-app-version" style="color:black;">')[1].split('</span>')[
                    0]
        return version
