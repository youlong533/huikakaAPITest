from Api_request import Api_request

def isSubscribe():
    r = Api_request()
    url = '/api/v1/wechat/isSubscribe'
    data= ''
    re =r.post_re(data,url)
    return re.text
isSubscribe()