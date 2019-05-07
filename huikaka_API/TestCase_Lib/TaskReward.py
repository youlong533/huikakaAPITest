from Api_request import Api_request

def task_reward():
    r = Api_request()
    url = '/api/v1/task/receiveReward'
    data = {
	"taskId":'9929'
}
    re = r.post_re(data,url)
    print(re.text)
    return re.text
task_reward()