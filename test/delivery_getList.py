import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "delivery.getList"


parameter = {
            'create_starttime':'2018-12-28 00:00:00',
            'page_no':'1',
            'page_size':10,
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


