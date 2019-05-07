import Api_request

def customer():
    r = Api_request.Api_request()
    url = '/api/v1/customer'
    data=''
    re =r.post_re(data,url)
    print(re.text)
    return re.text
customer()