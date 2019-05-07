from Api_request import Api_request

def transaction():
    r= Api_request()
    url = '/api/v1/account/transaction'
    data = {
	"pageIndex":'1',
	"pageSize":'20'
}
    re =r.post_re(data,url)
    print(re.text)
    return re.text
transaction()