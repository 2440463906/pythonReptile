import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_inventory.getList"
# 盘点查询

parameter = {
    'start_time' : '2019-01-01 00:00:00',
    'end_time' : '2019-10-10 00:00:00',
    'pda_token' : '4dac86652016327bdd327d1c4c836ed5',
    'device_code' : '1000000',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


