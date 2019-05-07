from Api_request import Api_request
#获取弹窗信息

def get_alert():
    r = Api_request()
    url = '/api/v1/alert/getalert'
    data = {
	"alertPosition":'201',
	"appVersion":'1',
	"osName":'wechat'
}
    re = r.post_re(data,url)
    return re.text
get_alert()