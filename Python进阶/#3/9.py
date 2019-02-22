class Doctor:
    def talk(self):
        self.salary = 100


# print(salary)

# 同样，实例变量self.salary也是局部变量


Doctor().talk()
print(salary)

# 即使执行了talk方法，也不能正确访问
# 因为它至始至终都是局部变量
