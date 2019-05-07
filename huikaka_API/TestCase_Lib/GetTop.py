from Api_request import Api_request

def get_top():
    r = Api_request()
    url = 'api/v1/loan/getTop'
    data = ''
    re = r.post_re(data,url)
    return re.text
get_top()