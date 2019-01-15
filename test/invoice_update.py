import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "invoice.update"


parameter = {
    'order_id' : '20181228160000001',
    'is_status' : 1,
    'print_time' : '2018-12-29 14:20:24',
    'tax_rate' : 0,
    'cost_tax' : 0,
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


