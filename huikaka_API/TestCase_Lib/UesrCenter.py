import Api_request

def user_center():
    data =''
    url = '/api/v1/customer/teamHistory'
    request = Api_request.Api_request()
    re = request.post_re(data,url)
    print(re.text)
    return re.text
user_center()