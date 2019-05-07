import Api_request

def my_team():
    request = Api_request.Api_request()
    url = '/api/v1/customer/team'
    data = {
	"pageIndex":'',
	"pageSize":''
}
    re = request.post_re(data,url)
    print(re.text)
    return re.text
my_team()