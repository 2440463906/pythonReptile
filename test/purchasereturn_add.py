import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "purchasereturn.add"


parameter = {
    'name' : '采购退货单1',
    'supplier_bn' : '111',
    'branch_bn' : 'stockhouse',
    'operator' : 'admin',
    'items' : '[{"bn":"00000001","price":"1","nums":"1"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


