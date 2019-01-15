import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pkg.getList"


parameter = {
            'page_no' : 1,
		    'page_size' : 10,
		    'items' : '[{"pkg_bn":"k0000001","pkg_name":"捆绑商品1","weight":"2","Products":"[{ "bn": "","name": "","nums": "","weight": "","price": ""}]"}]',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


