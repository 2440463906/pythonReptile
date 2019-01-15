import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service?from=qimen'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "order.addMemo"


parameter = {
            'start_time':'2018-12-28 00:00:00',
            'end_time':'2018-12-29 00:00:00',
            'page_no':'1',
            'page_size':10,
            'order_bn':'20181228160000001',
            'shop_bn':'taobao1',
    		'mark_text':'备注',
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


