try:
    raise Exception('主动抛出异常')
except Exception as e:
    print(e)
