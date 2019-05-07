import Api_request

def messagelist():
    request = Api_request.Api_request()
    data={
	"id":'1',
	"pageSize":'',
	"pageNo":''
    }
    url='/api/v1/message/messageList'
    re =request.post_re(data,url)
    print(re.text)
    return re.text
messagelist()