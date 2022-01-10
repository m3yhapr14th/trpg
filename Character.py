from Unit import *
from Enemies import *
from time import sleep

username = input("닉네임을 정하십시오. : ")
user = Unit(username, 1, 150, 50, 30, 5, "무직", 0)
print("> 이름: {0}".format(user.name))
sleep(0.5)
print("> 레벨: {0}".format(user.level))
sleep(0.5)
print("> 체력: {0}".format(user.hp))
sleep(0.5)
print("> 마나: {0}".format(user.mp))
sleep(0.5)
print("> 힘: {0}".format(user.power))
sleep(0.5)
print("> 방어력: {0}".format(user.defense))
sleep(0.5)
print("> 직업: {0}".format(user.job))
sleep(0.5)