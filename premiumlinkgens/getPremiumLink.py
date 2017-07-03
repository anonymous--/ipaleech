#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as sopa


def downloadLink(link):
    link = link.replace(':', '%3A').replace('//', '%2F%2F').replace('.net/', '.net%2F')
    site = "http://linkgenerate.com/link.php?link="
    token = '&token=LG'
    preDownloadLink = site + link + token
    data = requests.get(preDownloadLink).text
    soup = sopa(data, 'html5lib')
    return str(soup).split('href="')[1].split('" target')[0].replace(' ', '%25')
