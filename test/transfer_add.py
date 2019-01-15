import sys
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "transfer.add"


parameter = {
    'name' : '采购单1',				#采购单名称
    'vendor' : '123',					#供应商
    't_type' : 'E',								
    'branch_bn' : 'stockhouse',				#到货仓库编号
    'operator' : 'admin',						#经办人
    'memo'	: '备注',							#备注
    'items' : '[{"bn":"00000001","name":"商品1","nums":"2","price":"1"}]',	#货号 货品名称 数量  单价
            }








client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


