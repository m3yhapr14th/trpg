class Unit:
    def __init__(self, name, level, hp, mp, power, defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.power = power
        self.defense = defense
        

    def levelup(self):
        self.level += 1
        self.hp += 50
        self.mp += 50
        self.power += 10
        self.defense += 5
        print("{0}이(가) 레벨업을 하였습니다.".format(self.name))
        print("--[{0}]: 현재 스탯 정보--".format(self.name))
        print("> Level: {0}".format(self.level))
        print("> 체력: {0}".format(self.hp))
        print("> 마나: {0}".format(self.mp))
        print("> 힘: {0}".format(self.power))
        print("> 방어력: {0}".format(self.defense))

class User(Unit):
    def __init__(self, name, level, hp, mp, power, defense):
        Unit.__init__(self, name, level, hp, mp, power, defense)
        # level = 1
        # hp = 150
        # mp = 50
        # power = 30
        # defense = 5

    def CreateUser(self):
        self.name = input("닉네임을 정하십시오. : ")

class Job(Unit):
    def __init__(self, name, level, hp, mp, power, defense, job):
        Unit.__init__(self, name, level, hp, mp, power, defense)
        self.job = job