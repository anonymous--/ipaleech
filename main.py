#!/usr/bin/python3

from filehosts.dailyuploads import CheckFileIsOnline

raw_link = input('Please, Enter a link: ')

if raw_link.find('http') == -1:
    if raw_link.find('https') == -1:
        print("please try again.")
else:
    print(CheckFileIsOnline.check(site=raw_link))
