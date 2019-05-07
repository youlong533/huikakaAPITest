import Api_request

def bank_detail():
    request = Api_request.Api_request()
    url = "/api/v1/bank/getBankDetail"
    re =[]
    for i in range(1,39):
        if i not in ['25',26]:
            data = {
	        "bankId":i
        }
            d = request.post_re(data,url)
            re.append(d.text)
    print(re)
    return re
bank_detail()