from random import randint
import os

print ("哒哒哒，自动选择外卖！")
filename_list=[]
for filename in os.listdir(r'./data'):
    filename_len=len(filename)
    filename=filename[0:filename_len-4]
    filename_list.append(filename)
    print (filename)
filename_str=""
for i in filename_list:
    filename_str=filename_str+str(i)+" "
print ("目前支持",filename_str)
while (True):
    order_name=input("那你要点啥呢？ ")
    if order_name in filename_list:
        break
    else:
        print ("要点的现在还不支持哦！")



data_path='./data/'+order_name+'.txt'


order_list=[]


f=open(data_path,"r",encoding='utf8')
f.readline()
for line in f:
    if line[-1]=='\n':
        line_len=len(line)
        line=line[0:line_len-1]
    order_list.append(line)



order_len=len(order_list)

rand=randint(0,order_len-1)
print ("等会要不就点 "+ order_list[rand]+" 叭")

 



