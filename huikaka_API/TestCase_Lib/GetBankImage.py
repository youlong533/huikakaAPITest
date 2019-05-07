from Api_request import Api_request
from data_lib import data_lib

def get_bank_image():
    r = Api_request()
    url ='/api/v1/bank/getImage'
    data = {
	"token":data_lib.token,
	"bankId":'34'
}
    re =r.get_re(data,url)
    print(re.text)
    return re.text
get_bank_image()