import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_inventory.update"


parameter = {
    'pda_token' : '4dac86652016327bdd327d1c4c836ed5',
    'device_code' : '1000000',
    'inventory_bn' : 'PD1901040135',						
    'items' : '[{"bn":"00000001","num":"113"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


