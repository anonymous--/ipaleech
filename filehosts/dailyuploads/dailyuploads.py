#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as sopa


class CheckStatus(object):
    def __init__(self, appUrl):
        self.appUrl = appUrl

    def info(self):
        # sets the site for checking the link
        linkCheckSite = 'https://dailyuploads.net/?op=checkfiles'
        # sets the link for the file
        # sets the information needed to be sent to the post
        # linkURL = 'https://dailyuploads.net/7p2l61hsymgq'
        payload = {'list': self.appUrl, 'op': 'checkfiles', 'process': 'Check URLs'}
        # send the payload
        r = requests.post(linkCheckSite, payload)
        soup = sopa(r.text, 'html5lib')
        info = str(soup.find_all(attrs={'class': 'tbl1'}))
        return info

    def status(self):
        beginRemoval = str(self.info()).find('color')
        beginRemoval = beginRemoval + str(self.info())[beginRemoval:].find('>') + 1
        endRemoval = str(self.info()).rfind('</td><td>')
        ifFound = str(self.info())[beginRemoval:endRemoval]
        if ifFound == "Found":
            status = True
        elif ifFound == 'Not found!':
            status = False
        return status

    def fileSize(self):
        fileSize = str(self.info()).split('</td><td>')[1].split('</td>')[0]
        return fileSize
