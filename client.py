from urllib import parse,request
import json
import time
import hashlib
import urllib
import traceback

from get_sign import get_sign

class client:

      def client(self,url,parameter,obj,flag,token):


            thistime = time.time()

            textmod  = { 'flag':flag,
                        'type':"json",
                        'charset':'utf-8',
                        'ver':'1',
                        'timestamp':thistime,
                        'method':obj
                        }
                        
            textmod.update(parameter)

            # 签名
            si = get_sign(token)
            sign = si.get_sign(textmod)


            sign = {"sign":sign}
            textmod.update(sign)

            #将参数textmod进行编码
            textmod = urllib.parse.urlencode(textmod)
            textmod = textmod.encode("utf8")

            #模拟浏览器访问
            header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/x-www-form-urlencoded"}

            req = request.Request(url=url,data=textmod,headers=header_dict)
            res = request.urlopen(req)
            #读取返回值并转码
            res = res.read().decode("utf8")
            return res



