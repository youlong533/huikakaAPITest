import Api_request

def wechatconfig():
    request = Api_request.Api_request()
    data = ''
    url='/api/v1/configure/wechatConfig'
    re = request.post_re(data,url)
    print(re.text)
    return re.text
wechatconfig()