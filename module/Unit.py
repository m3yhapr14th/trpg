from random import *

class Unit:
    def __init__(self, name, level, hp, mp, power, defense, job, exp):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.power = power
        self.defense = defense
        self.job = job
        self.exp = exp
        
    def CreateUser(self):
        self.name = input("닉네임을 정하십시오. : ")

    def attack(self, enemy):
        self.enemy = enemy
        print("{0}: {1}에게 피해를 주었습니다. [공격력: {2}]".format(self.name, enemy, self.power))

    def damaged(self, damage):
        damage -= int(self.defense)
        self.hp -= damage
        print("{0}: {1}의 피해를 받았습니다.".format(self.name, damage))
        print("{0}의 현재 체력: {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}가 죽었습니다.".format(self.name))

    def expup(self):
        if self.exp == 100:
            self.level += 1
            self.hp += 50
            self.mp += 50
            self.power += 10
            self.defense += 5
            self.exp = 0
            print("{0}이(가) 레벨업을 하였습니다.".format(self.name))
            print("--[{0}]: 현재 스탯 정보--".format(self.name))
            print("> Level: {0}".format(self.level))
            print("> 체력: {0}".format(self.hp))
            print("> 마나: {0}".format(self.mp))
            print("> 힘: {0}".format(self.power))
            print("> 방어력: {0}".format(self.defense))

            if self.level == 2:
                print("스킬을 배웠습니다.\n => 칼날 베기: 공격력 {0}".format("힘+30"))

# class Skills(Unit):
#     def __init__(self):
        

# class Battle(Unit):
#     def __init__(self, enemy):
#         print("{0}와 전투를 시작합니다.".format(enemy))

#     # def damaged(self, power):
#     #     self.hp -= power
#     #     print("{0}: {1}에게 피해를 받았습니다.".format(self.name, power))
        

class Job(Unit):
    def __init__(self, name, level, hp, mp, power, defense, job):
        Unit.__init__(self, name, level, hp, mp, power, defense)
        self.job = False

    # def get_job(self):
