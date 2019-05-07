from Api_request import Api_request

def customer_qrcode():
    r= Api_request()
    url = '/api/v1/customer/qrcode'
    data = {
        'type':''
    }
    re =r.get_re(data,url)
    print(re.text)
    return re.text
customer_qrcode()