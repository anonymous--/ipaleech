# import json
from unshortenit import unshorten

from filehosts.dailyuploads import dailyuploads
from premiumlinkgens.getPremiumLink import downloadLink as downloadLink


def check(site):
    host = str(site).split('.net')[0].split('https://')[1]
    testme = dailyuploads.CheckStatus(site)

    if testme.status() is True:
        outPut = downloadLink(unshorten(site))
    elif testme.status() is False:
        outPut = False
        # outPut = "Can't find file!"
    return outPut
