import Api_request
from data_lib import data_lib

def bank_list():
    r = Api_request.Api_request()
    url = '/api/v1/bank'
    data={
	"token":data_lib.token
}
    re = r.post_re(data,url)
    print(re.text)
    return re.text
bank_list()