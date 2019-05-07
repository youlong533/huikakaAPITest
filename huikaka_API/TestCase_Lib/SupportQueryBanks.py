from Api_request import Api_request

def support_query_banks():
    r= Api_request()
    url = '/api/v1/bankConfig/support/query/banks'
    data = {
	"id":'',
	"name":'',
	"logo":''
}
    re = r.post_re(data,url)
    print(re.text)
    return re.text
support_query_banks()
