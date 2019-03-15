import urllib.request
import random
iplist=['114.101.134.96:61234','60.177.224.244:18118','183.159.89.11:18118']
url='http://www.whatismyip.com.tw/'
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener=urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
