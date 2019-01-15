import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = " pda_user.cancel"


parameter = {
    'pda_token' : 'fe3fc487663e1d0a0d7172a40770481d',
    'device_code' : '1000000',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


