# Adventures on Hacking
# Tor proxy
# by Paulo Francisco

# Imports
import requests

# Default conf
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

# Make a post request
def postReq(url,data={},headers=None):
    global session
    if(headers!=None):
        return session.post("url",data=data,headers=headers)
    else:
        return session.post("url",data=data)
# Make a get request
def getReq(url,headers=None):
    global session
    if(headers!=None):
        return session.get("url",headers=headers)
    else:
        return session.get("url")
