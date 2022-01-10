from Unit import *

username = input("닉네임을 정하십시오. : ")
user = User(username, 1, 150, 50, 30, 5)
print("> 이름: {0}\n> 레벨:{1}\n> 체력:{2}\n> 마나:{3}\n> 힘:{4}\n> 방어력:{5}"\
    .format(user.name, user.level, user.hp, user.mp, user.power, user.defense))

while user.level <= 98:
    user.levelup()