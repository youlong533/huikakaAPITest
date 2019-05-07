import os

#调用所有接口
lst = os.listdir(os.getcwd())

for c in lst:
    if os.path.isfile(c) and c.endswith('.py') and c.find("__main__")==-1:
        print(c)
        #os.system(os.path.join(os.getcwd(),c))
        os.system("python ./%s" % c)