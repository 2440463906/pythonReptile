import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "invoice.getList"


parameter = {
		    'start_time' : '2018-12-28 00:00:00',
		    'end_time' : '2018-12-30 00:00:00',
		    'status' : 0,
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


