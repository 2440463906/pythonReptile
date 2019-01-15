import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "stock.getDetailList"


parameter = {
            'page_no':'1',
            'page_size':10,
            'goods_bn':'00000001',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


