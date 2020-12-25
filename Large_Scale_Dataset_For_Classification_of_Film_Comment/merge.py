import os
import random


data=[]
file_list=[]
#file_list=os.path.abspath(__file__)
root_path=os.getcwd()
print (root_path)
file_list=os.listdir(root_path)
file_list_len=len(file_list)
data=[]
for i in range (file_list_len):
    tmp_file=file_list[i]
    if tmp_file[0:4]=='data':
        with open(os.path.join(root_path,tmp_file),'r',encoding='utf-8',errors='ignore') as f:
            tmp_data=f.readlines()
        data=data+tmp_data
random.shuffle(data)

with open('data.txt','w',encoding='utf-8',errors='ignore') as f:
    f.writelines(data)