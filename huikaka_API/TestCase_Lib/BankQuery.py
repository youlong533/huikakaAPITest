import Api_request

def bank_query():
    request = Api_request.Api_request()
    data={
	"id":'1',
	"name":'',
	"logo":''
}
    url ='/api/v1/bankConfig/support/query/banks'
    re = request.post_re(data,url)
    return re.text
bank_query()