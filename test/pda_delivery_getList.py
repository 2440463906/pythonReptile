import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_delivery.getList"


parameter = {
    'pda_token' : 'a32ef010147d2f854609c06fb54aefd8',
    'device_code' : '1000000',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


