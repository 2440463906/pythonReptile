import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_iostock.getList"
# 出入库单   需要先审核


parameter = {
    'pda_token' : '62d1e64eac5628c29e773f2e1aaa4146',
    'device_code' : '1000000',
    'io_type' : 7,
    'start_time':'2018-12-01',
    'end_time':'2019-12-01',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


