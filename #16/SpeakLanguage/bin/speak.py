import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))  # 获取项目目录

sys.path.append(BASE_DIR)  # 将项目目录添加到模块的搜索列表里

if __name__ == '__main__':
    from speak_language.main import run  # 从源代码入口程序main.py中导入run方法

    run()  # 执行
