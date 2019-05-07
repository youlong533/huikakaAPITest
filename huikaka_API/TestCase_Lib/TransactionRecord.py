from Api_request import Api_request

def transaction_record():
    r = Api_request()
    url = '/api/v1/account/withdraw/transaction'
    data = {
	"isAll":True,
	"pageIndex":'1',
	"pageSize":'1'
}
    re =r.post_re(data,url)
    print(re.text)
    return re.text
transaction_record()
