from Api_request import Api_request

def wechat_configure():
    r= Api_request()
    url = '/api/v1/wechat/share/configure'
    data = {
	"url":'http://hkkwx.xinhuixuan.cn/kakaka-wechat-customer/api/v1/bankConfig/support/query/banks'
}
    re = r.post_re(data ,url)
    print(re.text)
    return re.text
wechat_configure()