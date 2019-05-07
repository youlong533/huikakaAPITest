from Api_request import Api_request

def creat_bank_order():
    r= Api_request()
    url = '/api/v1/bank/createBankOrder'
    data = {
	"bankId":'34',
	"osName":'wechat',
	"otherOrder":'0'
}
    re =r.post_re(data,url)
    print(re.text)
    return re.text
creat_bank_order()