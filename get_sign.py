import hashlib

class get_sign:
    def __init__(self,token):
        self.token = token

    def get_sign(self,params):
        sign = self.get_sign_str(params)
        sign = self.get_md5(sign).upper()
        sign = self.get_md5(sign+str(self.token))
        return sign.upper()

    def get_sign_str(self,params):
        sign = ''
        if type(params) == dict:
            sign = self.get_value_str(params)
        return sign

    def get_value_str(self,value):
        if type(value) == list:
            value = dict(zip(range(len(value)),value))
        if type(value) == dict:
            value = self.do_dict(value)
        return value

    def do_dict(self,dic):
        s = ''
        keys = sorted(dic)
        for key in keys:
            value = self.recursive(dic[key])
            s = s + str(key) + str(value)
        return s

    def recursive(self,value):
        if type(value) == dict:
            return self.get_value_str(value)
        if type(value) == list:
            return self.get_value_str(value)
        return value

    def get_md5(self,string):
        try:
            m = hashlib.md5()
            m.update(string.encode(encoding='utf-8'))
            dest = m.hexdigest()
            return dest
        except:
            return False
