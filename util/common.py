# coding:utf-8
# author:ila
import hashlib
# 对密码进行md5加密
class Common(object):
    def md5(self, pwd):
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        return md5.hexdigest()
