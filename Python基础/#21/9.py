class MSException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


try:
    raise MSException('这是MinuteSheep自定义的异常')
except Exception as e:
    print(e)
