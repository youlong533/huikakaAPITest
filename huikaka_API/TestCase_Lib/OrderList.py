import  Api_request

def orderlist():
    data ={
	"cardType":'CARD',
	"keyword":'',
	"pageNo":1,
	"pageSize":10,
	"showTrash":0,
	"status":'null'
	}
    request = Api_request.Api_request()
    url = '/api/v1/orderRecord/listV2'
    re = request.post_re(data,url)
    print(re.text)
    return re.text
orderlist()