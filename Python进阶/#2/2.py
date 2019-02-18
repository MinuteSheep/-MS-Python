def maxNum(nums):
    '''
    返回nums中的最大数字
    '''
    max_num = nums[0]
    for i in nums:
        if max_num < i:
            max_num = i
    print(max_num)


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 3, 1, 5, 5, 3, 1]
list3 = [23, 456, 134, 45]

maxNum(list1)
maxNum(list2)
maxNum(list3)


# 使用函数极大的提高了代码的重复利用率
