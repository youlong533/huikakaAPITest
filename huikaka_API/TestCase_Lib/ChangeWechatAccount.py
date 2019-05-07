from Api_request import Api_request

class change_wechat_account:
    r = Api_request()
    url = '/api/v1/customer'
    data = {
	"wechatAccount":'youlong533'
}
    r.put_re(data,url)