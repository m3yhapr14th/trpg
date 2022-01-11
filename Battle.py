from Unit import *
from Enemies import *
from func import *
from Character import *
from time import sleep


class Battle():
    def __init__(self):
        print("{0}이 길을 가다가 {1}를 마주쳤다.".format(user.name, Hydra.name))
        sleep(1)
        print("[{0} 출몰]\n[레벨: {1}, 체력: {2}, 공격력: {3}, 방어력: {4}]".format(Hydra.name, Hydra.level, Hydra.hp, Hydra.power, Hydra.defense))
        sleep(0.5)
        # 전투
        answer = input("전투를 시작하겠습니까?\n1. 전투 시작\n2. 도망\n선택: ")
        if answer == '1':
            while Hydra.hp > 0:
                if user.hp > 0:
                    battle = input("1. 공격\n2. 도망가기\n선택: ")
                    if battle == '1':
                        user.attack(Hydra.name)
                        sleep(0.2)
                        Hydra.damaged(user.power)
                        sleep(1)
                        if Hydra.hp > 0:
                            Hydra.attack(user.name)
                            sleep(0.2)
                            user.damaged(Hydra.power)
                            sleep(1)
                        else:
                            break
                    else:
                        print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))
                        break
                else:
                    game_over()
                    exit()
            user.exp += Hydra.exp
            user.expup()

        elif answer == '2':
            print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))

        else:
            game_over()
            exit()

# print("{0}이 길을 가다가 {1}를 마주쳤다.".format(user.name, Hydra.name))
# sleep(1)
# print("[{0} 출몰]\n[레벨: {1}, 체력: {2}, 공격력: {3}, 방어력: {4}]".format(Hydra.name, Hydra.level, Hydra.hp, Hydra.power, Hydra.defense))
# sleep(0.5)
# # 전투
# answer = input("전투를 시작하겠습니까?\n1. 전투 시작\n2. 도망\n선택: ")
# if answer == '1':
#     while Hydra.hp > 0:
#         if user.hp > 0:
#             battle = input("1. 공격\n2. 도망가기\n선택: ")
#             if battle == '1':
#                 user.attack(Hydra.name)
#                 sleep(0.2)
#                 Hydra.damaged(user.power)
#                 sleep(1)
#                 if Hydra.hp > 0:
#                     Hydra.attack(user.name)
#                     sleep(0.2)
#                     user.damaged(Hydra.power)
#                     sleep(1)
#                 else:
#                     break
#             else:
#                 print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))
#                 break
#         else:
#             game_over()
#             exit()
#     user.exp += Hydra.exp
#     user.expup()

# elif answer == '2':
#     print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))

# else:
#     game_over()

# print("{0}이 길을 가다가 {1}를 마주쳤다.".format(user.name, Hydra_Lv2.name))
# sleep(1)
# print("[{0} 출몰]\n[체력: {1}, 공격력: {2}, 방어력: {3}]".format(Hydra_Lv2.name, Hydra_Lv2.hp, Hydra_Lv2.power, Hydra_Lv2.defense))
# sleep(0.5)
# # 전투
# answer = input("전투를 시작하겠습니까?\n1. 전투 시작\n2. 도망\n선택: ")
# if answer == '1':
#     while Hydra_Lv2.hp > 0:
#         battle = input("1. 공격\n2. 스킬\n3. 도망가기\n선택: ")
#         if battle == '1':
#             user.attack(Hydra_Lv2.name)
#             sleep(0.2)
#             Hydra_Lv2.damaged(user.power)
#             sleep(1)
#             Hydra_Lv2.attack(user.name)
#             sleep(0.2)
#             user.damaged(Hydra_Lv2.power)
#             sleep(1)
#         elif battle == '2':
#             if user.mp < 50:
#                 print("스킬을 사용할 수 없습니다.")
#             else:
#                 print("{0}: 죽음은 바람과 같지..퓨슝빠슝".format(user.name))
#                 user.power += 30
#                 user.attack(Hydra_Lv2.name)
#                 sleep(0.2)
#                 user.mp -= 50
#                 Hydra_Lv2.damaged(user.power)
#                 user.power -= 30
#                 sleep(1)
#         elif battle == '3':
#             print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))
#             break
#     user.exp += Hydra_Lv1.exp
#     user.expup()

# elif answer == '2':
#     print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))

# else:
#     game_over()

# print("{0}이 길을 가다가 {1}를 마주쳤다.".format(user.name, Hydra_Lv3.name))
# sleep(1)
# print("[{0} 출몰]\n[체력: {1}, 공격력: {2}, 방어력: {3}]".format(Hydra_Lv3.name, Hydra_Lv3.hp, Hydra_Lv3.power, Hydra_Lv3.defense))
# sleep(0.5)
# # 전투
# answer = input("전투를 시작하겠습니까?\n1. 전투 시작\n2. 도망\n선택: ")
# if answer == '1':
#     while Hydra_Lv3.hp > 0:
#         battle = input("1. 공격\n2. 스킬\n3. 도망가기\n선택: ")
#         if battle == '1':
#             user.attack(Hydra_Lv3.name)
#             sleep(0.2)
#             Hydra_Lv3.damaged(user.power)
#             sleep(1)
#             Hydra_Lv3.attack(user.name)
#             sleep(0.2)
#             user.damaged(Hydra_Lv3.power)
#             sleep(1)
#         elif battle == '2':
#             if user.mp < 50:
#                 print("스킬을 사용할 수 없습니다.")
#             else:
#                 print("{0}: 죽음은 바람과 같지..퓨슝빠슝".format(user.name))
#                 user.power += 30
#                 user.attack(Hydra_Lv3.name)
#                 sleep(0.2)
#                 user.mp -= 50
#                 Hydra_Lv3.damaged(user.power)
#                 user.power -= 30
#                 sleep(1)
#         elif battle == '3':
#             print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))
#             break
#     user.exp += Hydra_Lv1.exp
#     user.expup()

# elif answer == '2':
#     print("{0}가 줄행랑을 쳤다. 멍청한 자식".format(user.name))

# else:
#     game_over()