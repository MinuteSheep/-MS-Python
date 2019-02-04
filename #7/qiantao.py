# # for循环嵌套
# for i in range(10):
#     for p in range(5):
#         print(p)

# # 可以看到输出了10次0，1，2，3，4

# # while循环嵌套
# num = 5
# while num < 7:
#     while num < 6:
#         print('hello~~~')
#         num += 1
#     print('hi~~~~')
#     num += 1

# while 和 for 循环嵌套
num = 5
while num < 8:
    for i in range(3):
        print(i)
    num +=1

# 可以看到输出了3次0，1，2