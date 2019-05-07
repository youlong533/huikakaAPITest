from Api_request import Api_request

def get_levitated_sphere():
    r = Api_request()
    url = '/api/v1/task/getLevitatedSphere'
    data = ''
    re =r.post_re(data,url)
    return re.text
get_levitated_sphere()