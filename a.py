n=0
dic={'admin':'123','lisi':'456','zhangsan':'789'}
while 1:
    name=input('请输入你的名字：')
    if len(name)==0 or name not in dic.keys():
        file = open('E:\\datebase.txt','a')
        file.write(name+'\n')
        file.close()
        print('你的输入有误，请重新输入')
        
    
