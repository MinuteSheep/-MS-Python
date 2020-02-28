'''
从下列段落中提取出所有数字，并输出
本例结果应该是：49737
'''
import re


test = ''' JAKARTA, Indonesia—Flag carrier Garuda Indonesia said it is seeking to cancel an order for 49 Boeing Co. 737 MAX jets, saying passengers have lost confidence in the aircraft following two deadly crashes in recent months.  '''

# pattern = re.compile('\d')
pattern = re.compile('\d+')

result = re.findall(pattern, test)
print(result)

print(result[0] + result[1])
