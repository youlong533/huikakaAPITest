from Api_request import Api_request

def captcha_image():
    r = Api_request()
    url = '/api/v1/captcha/image'
    #type必填，验证码类型(1,登录、2:提现,3:注册,4:完善银行卡,5:添加办卡人信息,6:更换手机号码-原手机号码.7:更换手机号码-新手机号码),8:车险申请-校验被保人,9:保险申请-校验被保人 10:信用卡申请，11贷款申请--待补充
    data = {
	"mobile":'18801482265',
	"type":'10',
	"deviceId":'',
	"deviceModel":'',
	"osName":'',
	"osVersion":'',
	"appChannel":'',
	"appVersion":''
}
    re = r.get_re(data,url)
    print(re.text)
captcha_image()
