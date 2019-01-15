import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "appropriation.add"


parameter = {
    'appropriation_type' : '出入库调拨',
    'from_branch' : '我的仓库',
    'to_branch' : '仓库2',
    'operator' : 'admin',
    'items' : '[{"bn":"00000001","nums":"1"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


