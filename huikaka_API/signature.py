import base64,hashlib
import csv,requests,json,data_lib

# 生成签名
# 签名规则如下： str = 请求参数进行顺序排列再进行拼接
# sign = md5(base64(timestamp) + token + 私密 + str)
#
# @ param
# request
# HTTP请求
# @ return 签名
class signature():
    timestamp = data_lib.data_lib.timestamp
    #timestamp = '1555299128'
    #print(timestamp)
    time = base64.b64encode(bytes(timestamp.encode('utf-8')))
    #print(type(time))
    token =data_lib.data_lib.token
    #私密
    key ="56255fde5b5bd28dd983ee7531d98d9565f2"

#获取原始请求
#    def re_http(self):

#获取请求参数并进行名称排序




#组装签名字符串
    def str_url(self):
        order_param = 'orderId'+'173762823385620480'+'bankId'+'10'
        str_url = str(self.time)+self.token+self.key+order_param
        return str_url
#生成签名
    def sign(self,url):
        self.url = url
        m = hashlib.md5()
        m.update(self.url.encode('utf-8'))
        sign = m.hexdigest()
        #print(sign)
        return sign

    def s(self):
        s = signature()
        url = s.str_url()
        sign = s.sign(url)
        return sign

#signature().s()
#s = signature()
#url = s.str_url()
#s.sign(url)


#将timestamp和signature数据存入CSV文件中
csv_file = open('E:\\params\\order.csv','w',newline='',encoding='utf-8')
write = csv.writer(csv_file)
write.writerow(['timestamp','token','signature'])
write.writerow([signature.timestamp,signature.token,signature().s()])