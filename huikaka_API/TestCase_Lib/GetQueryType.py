from Api_request import Api_request

def get_query_type():
    r = Api_request()
    url = '/api/v1/bankConfig/getQueryType'
    data = {
	"orderId":'173762823385620480',
	"bankId":'10'
}
    re = r.post_re(data,url)
    return re.text
get_query_type()