import sys
import hashlib
sys.path.append(r'../')
from client import client

url   = 'http://www.yunqi.com/index.php/openapi/rpc/service'
flag  = 'test'
token = 'OaYMGiaNlXXsspjnsnTjzjrDCYWngEkh'


obj  = "pda_user.confirm"



parameter = {
    'user_name' : 'admin',
    'password' : 'admin123',
    'device_code' : '1000000',
            }



# md5加密 密码
m = hashlib.md5()
m.update(parameter['password'].encode(encoding='utf-8'))
parameter['password'] = m.hexdigest()






client = client()
cli = client.client(url,parameter,obj,flag,token)
print(cli)


