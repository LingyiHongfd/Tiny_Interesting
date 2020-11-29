#小六壬占卜，自动起卦
#任意输入数字，至少为3个数字 月日时，也可以多个数字起卦
#输出起卦结果，需要自行解卦


hexagram=['大安','留连','速喜','赤口','小吉','空亡']
meaning=['大吉','小凶','小吉','小凶','小吉','大凶']

numbers=0
input_number=[]
print('本程序为小六壬占卜自动起卦')
mode=input('是否默认月日时起卦？是输入 1 ，否输入 0 ：  ')

mode=int(mode)

if mode==1:
    numbers=3
else:
    numbers=int(input('非默认月日时起卦，请输入数字数量： '))


if mode==1:
    num=int(input('请输入月：'))
    input_number.append(num)
    num=int(input('请输入日：'))
    input_number.append(num)
    num=int(input('请输入时：'))
    input_number.append(num)
else:
    for i in range (numbers):
        input_str='请输入第 '+str((i+1))+' 个数字：'
        num=int(input(input_str))
        input_number.append(num)
#print (input_number)

output=[]
ans=1
output_str='起卦结果是： '

for i in range(len(input_number)):
    value=input_number[i]
    ans=ans+value-1
    r=(ans%6)
    output.append(hexagram[r-1])
    output_str=output_str+'  '+hexagram[r-1]

print (output_str)
stop=input()























