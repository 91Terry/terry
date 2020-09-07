import random
color = ['梅花','黑桃','方块','红心']
num = list(range(1,14))
cad = []
user_cad = {}
count = 0
user = input('请输入姓名:').strip()#用户输入姓名，用逗号隔开
user = list(user.split(','))
for i in color:
    for j in num:
        c = f'{i}*{j}'
        cad.append(c)
for people in user:
    people_cad = (",".join(random.sample(cad,3))).split(',')
    user_cad[people] = people_cad

    for i in people_cad:
        cad.remove(i)
    count+=1
print(user)
print(user_cad)
print(f"共有{len(user)}个玩家,还剩{len(cad)}张牌")


