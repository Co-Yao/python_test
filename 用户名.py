import time


# 创建一个用户类
class Person(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    # 创建一个方法，可以休眠五分钟
    @staticmethod
    def get_sleep():
        time.sleep(300000)


if __name__ == '__main__':
    user_name = input('输入你的用户名')
    user_password = input('输入你的用户密码')
    # 创建一个用户，传入用户名和密码
    user_name = Person(user_name, user_password)
    # 计时器，记录输入的次数
    count = 1
    # 如果输入错误循环执行代码
    while True:
        # 登录时输入的用户名和密码
        a, b = input('输入你的用户名和密码，中间用空格分隔：').split(' ')
        # 判断是否跟创建的用户名跟密码是否一致
        if a == user_name.name and b == user_name.password:
            print('登录成功')
            # 登录成功跳出循环
            break
        else:
            # 不一致时就判断是否输入超过三次
            if count <= 3:
                count += 1
                print('用户名或密码输入错误，请重试')
            # 如果超过三次就让其休息三秒,在从新输入
            else:
                print('输入的错误次数过多,请5分钟之后再试!')
                user_name.get_sleep()
                count = 1




