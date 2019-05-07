import Api_request

def message_type_list():
    request = Api_request.Api_request()
    data = ''
    url = '/api/v1/message/messageTypeList'
    re = request.post_re(data,url)
    print(re.text)
    return re.text
message_type_list()