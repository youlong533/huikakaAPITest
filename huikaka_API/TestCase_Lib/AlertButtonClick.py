from Api_request import Api_request
#点击弹窗

def alert_button_click():
    r= Api_request()
    url = '/api/v1/alert/alertBtnClick'
    data = {
	"osName":'',
	"alertId":''
}
    re = r.post_re(data,url)
    return re.text
alert_button_click()