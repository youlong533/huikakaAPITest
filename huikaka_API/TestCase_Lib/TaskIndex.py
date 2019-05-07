from Api_request import Api_request

def task_index():
    r = Api_request()
    url = '/api/v1/task/index'
    data = {
	"osName":'wechat'
}
    re = r.post_re(data,url)
    print(re.text)
    return re.text
task_index()