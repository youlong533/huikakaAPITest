import csv,time

class data_lib():
    #host = input("输入域名：")
    host = "http://hkka.xinhuixuan.cn/kakaka-wechat-customer"
    #host = "http://testqkkapi.kakahui.net/kakaka-wechat-customer"
    #name = input("输入参数名称：")
    name = 'name'
    #data = input("输入参数值：")
    data = '123'
    #token = input("输入token：")
    #token = "fd66c4b4bf339cefc38ff35e6de54cf4"
    token ="589a4af19fb25883adec29825d905795"
    timestamp =str(int(time.time()))


#存储数据
    def save_data(self,name,data):
        name = self.name
        data = self.data
        with open('E:\\params\\data.csv','w+',newline='',encoding='utf-8') as file:
            write = csv.writer(file)
            write.writerow([name,data])

#读取数据
    def read_data(self,name):
        name = self.name
        with open('E:\\params\\data.csv','r') as flie:
            read = csv.reader(flie)
            for param in read:
                print(param)
            return param
#dl = data_lib()
#dl.save_data(data_lib.name,data_lib.data)
#dl.read_data(data_lib.name)
#print(data_lib.timestamp)