import random
import string
count = 0
cars_num = []
while count<3:
    for i in range(20):
        a = "".join(random.sample(string.ascii_uppercase+string.digits,5))   #随机生成后5个字母和数字
        b = "".join(random.choice(string.ascii_uppercase))      #随机生成第一个字母 "".join()将列表元素拼接
        car = f'京{b}-{a}'
        print(i+1,car)
        cars_num.append(car)
    print(f'你有{3-count}次机会选择')
    choose = input('输入你喜欢的号码：').strip()
    if choose in cars_num:
        print(f'恭喜你获得新的号码{choose}')
        break
    else:
        print('输入有误，请重新选择')
    count += 1

