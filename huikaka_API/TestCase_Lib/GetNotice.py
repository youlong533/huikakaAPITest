import Api_request

def getNotice():
    request = Api_request.Api_request()
    url = '/api/v1/message/getNotice'
    data ={
	"id":'1'
    }
    re =request.get_re(data,url)
    print(re.text)
    return re.text
getNotice()