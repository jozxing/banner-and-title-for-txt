#encoding:utf-8
import requests
import re
import sys
import os


#解决ascii 码无法兼容utf-8 问题
reload(sys)  
sys.setdefaultencoding('utf-8') 

target=sys.argv[1]
def readtxt():  
    bc = open(target)  
    for line in bc.readlines(): 
        cccc="http://"+line
        aaaa=cccc.replace('\n', '')
        try:
            response=requests.get(aaaa, timeout=3)
            serverText = response.headers['server']
            titleText = re.findall(r'<title>(.*?)</title>',response.text)[0] 
            
            if len(serverText) > 0:
                result = aaaa  + " ----  " + serverText + " ---- " + titleText + "\n"
                print result
        except:
            pass
        with open("result.txt","a")  as  res: 
            res.write(result)
if __name__ == '__main__':
    readtxt()
   