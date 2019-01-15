import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_pick.getStockList"
# 备货单		排除已拣货  已领取

parameter = {
    'pda_token' : '62d1e64eac5628c29e773f2e1aaa4146',
    'device_code' : '1000000',
    'status' : 'ready',
    'page_no' : 1,
    'page_size' : 10,
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


