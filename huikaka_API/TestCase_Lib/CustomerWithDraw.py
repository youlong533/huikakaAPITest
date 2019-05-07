from Api_request import Api_request

def customer_with_draw():
    r = Api_request()
    url = '/api/v1/configure/customerWithdraw/json'
    data=''
    re =r.get_re(data,url)
    print(re.text)
    return re.text
customer_with_draw()