import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "goods.add"


parameter = {
    'goods_name' : '商品4',
    'product_bn' : '00000004',
    'barcode' : '00000004',
    'products' : '[{"bn":"10001010","name":"货物1","barcode":"10001010"}]',

            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


