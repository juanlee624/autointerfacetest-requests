#!/usr/bin/env python
#coding:utf-8
import requests,json
url="http://172.16.100.253:38181/target-analysis/orm/userInfo"
headers={
  "Host": "172.16.100.253:38181",
  "Connection":"keep-alive",
  "Pragma":"no-cache",
  "Cache-Control":"no-cache",
  "Accept":"application/json, text/plain, */*",
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Referer":"http://172.16.100.253:38181/target-analysis/",
  "Accept-Encoding":"gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.8",
  "Cookie":"JSESSIONID=A3646F711E518E94F4D0894C5AA33C89"
         }
prams={
}
#response=requests.get(url,data=json.dumps(prams), headers=headers)
response=requests.request("get",url,data=json.dumps(prams),headers=headers)
print(response.text)