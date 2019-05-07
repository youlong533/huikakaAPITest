from Api_request import Api_request

def account():
    r= Api_request()
    url = '/api/v1/account'
    data = ''
    re = r.post_re(data,url)
    print(re.text)
    return re.text
account()