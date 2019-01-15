import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "branch.position"


parameter = {
    'branch_bn' : 'stockhouse',
    'items' : '[{"bn":"00000001","position":"货位1"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


