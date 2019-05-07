import Api_request

def my_customer():
    request = Api_request.Api_request()
    url = '/api/v1/customer/team/customer'
    data ={
	"pageIndex":'',
	"pageSize":''
}
    re = request.post_re(data,url)
    return re.text
my_customer()