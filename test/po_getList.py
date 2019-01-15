import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "po.getList"

parameter = {
            'po_bn':'201812291217009142',
            'page_no':'1',
            'page_size':10,
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


