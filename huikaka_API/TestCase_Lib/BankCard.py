import Api_request

def bank_card():
    r= Api_request.Api_request()
    url = '/api/v1/account/bank/card'
    data = ''
    re = r.post_re(data,url)
    #print(re.text)
    return re.text
bank_card()