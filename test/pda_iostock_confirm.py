import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_iostock.confirm"


parameter = {
    'pda_token' : '62d1e64eac5628c29e773f2e1aaa4146',
    'device_code' : '1000000',
    'io_type' : 70,
    'io_bn' : 'E20190102000003',
    'io_status' : 'FINISH',
    'items' : '[{"bn":"00000001","nums":"1"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


