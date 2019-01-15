import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "goods.edit"


parameter = {
    'product_bn' : '00000001',
    'sale_price' : '66',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


