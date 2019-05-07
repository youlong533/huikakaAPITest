import Api_request
#获取系统时间

def systemtime():
    request = Api_request.Api_request()
    url = '/api/v1/configure/systemTime'
    data = ''
    re = request.get_re(data,url)
    print(re.text)
    return re.text
systemtime()