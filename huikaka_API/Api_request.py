import requests,json
import data_lib
from signature import signature

class Api_request:
    dl = data_lib.data_lib()
#生成接口链接地址
    def link(self,url):
        link = self.dl.host +url
        return link
    headers = {'content-type': 'application/json;charset=UTF-8', 'token': dl.token,'timestamp':dl.timestamp,'signature':signature().s()}
   # headers2 = {'content-type': 'application/json;charset=UTF-8', 'token': dl.token,'timestamp':dl.timestamp2}
    #print(link)

#POST请求(时间戳为string型）
    def post_re(self,post_param,url):
        d = post_param
        post_re = requests.post(self.link(url),data=json.dumps(d),headers=self.headers)
        #print(post_re.text)
        return post_re

#POST请求（时间戳为int型）
#    def post2_re(self,post_param,url):
#        d = post_param
#        post_re = requests.post(self.link(url),data=json.dumps(d),headers=self.headers2)
#        print(post_re.text)
#        return post_re
#GET请求
    def get_re(self,get_param,url):
        d = get_param
        get_re = requests.get(self.link(url),data=json.dumps(d),headers=self.headers)
        #print(get_re.text)
        return get_re

#PUT请求
    def put_re(self,put_param,url):
        d = put_param
        put_re = requests.put(self.link(url),data=json.dumps(d),headers=self.headers)
        #print(put_re.text)
        return put_re