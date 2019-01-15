import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_pick.bindbox"


parameter = {
    'pda_token' : '62d1e64eac5628c29e773f2e1aaa4146',
    'device_code' : '1000000',
    'items' : '[{"delivery_bn":"1901030000001","basket_no":"1231234656"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


