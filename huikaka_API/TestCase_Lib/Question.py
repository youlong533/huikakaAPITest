import Api_request

def question():
    r= Api_request.Api_request()
    url = '/api/v1/question'
    data = ''
    re = r.post_re(data,url)
    print(re.text)
    return re.text
question()