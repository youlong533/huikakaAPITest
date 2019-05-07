import Api_request

def my_parent():
    r = Api_request.Api_request()
    url = '/api/v1/customer/parent'
    data = ''
    re = r.post_re(data,url)
    print(re.text)
    return re.text
my_parent()