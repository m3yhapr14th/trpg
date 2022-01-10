from Unit import *
from Enemies import *
from game_func import *
from Character import *


game_start()

print("{0}이 길을 가다가 {1}를 마주쳤다.".format(user.name, Hydra.name))
# 전투
answer = input("전투를 시작하겠습니까?\n1. 전투 시작\n2. 도망\n선택: ")
if answer == '1':
    while Hydra.hp > 0:
        battle = input("1. 공격\n2. 도망가기\n선택: ")
        if battle == '1':
            user.attack(Hydra.name)
            Hydra.damaged(user.power)
            if Hydra.hp <= 0:
                user.exp += Hydra.exp
                user.expup()
        elif battle == '2':
            print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))
            break

elif answer == '2':
    print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))

else:
    game_over()