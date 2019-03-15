import urllib.request
import urllib.parse
import json
content=0
while True:
    if content!='end':
        content=input()
        url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        head={}
        head['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
        data={}
        data={'action':'FY_BY_CLICKBUTTION',
              'client':'fanyideskweb',
              'doctype':'json',
              'from':'AUTOkeyfrom	fanyi.web',
              'salt':'1524049808849',
              'sign':'0f8d84e0cba3c8a6b352432091329ad6',
              'smartresult':'dict',
              'to':'AUTO',
              'typoResult':'false',
              'version':'2.1'}
        data['i']=content
        data=urllib.parse.urlencode(data).encode('utf-8')
        respones=urllib.request.urlopen(url,data)
        html=respones.read().decode('utf-8')
        target=json.loads(html)
        print('%s'%(target['translateResult'][0][0]['tgt']))
    else:
        break