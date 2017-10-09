import random, time

class Character(object):
    def __init__(self, ID, Health):
        self.attribution = {
        'ID' : ID,
        # 'NAME' : 'Aura',
        # 'ROLE' : 'Medic',
        'HEALTH' : Health,
        # 'ABILITY' : 'Healstation',
        }
    #
    # def get_intro(self):
    #     print('%s the %s. Yadda yadda heals the ill shoots the healthy, Are we done?' %(
    #     self.attribution['NAME'],
    #     self.attribution['ROLE']))
    def healing(self, heal):
        if heal == 3:
            self.attribution['HEALTH'] += 3
            print('%s healed 3 HP' %self.attribution['ID'])
        else:
            pass

    def healing2(self, heal2):
        if heal2 == 3:
            self.attribution['HEALTH'] += 3
            print('%s healed 3 HP' %self.attribution['ID'])
        else:
            pass


    def attack(self, other):
        self.other = other
        if random.randint(0,10) in [0, 1, 2, 3, 4]:
            DAMAGE = random.randint(2,10)
            self.other.attribution['HEALTH'] -= DAMAGE
            print('%s was attacked (%2sDamage) by %s' %(
            self.other.attribution['ID'],
            DAMAGE,
            self.attribution['ID']))
        elif random.randint(0,10) in [5, 6, 7]:
            DAMAGE = random.randint(20,35)
            self.other.attribution['HEALTH'] -= DAMAGE
            print('%s was attacked (%2s Critical Damage) by %s' %(
            self.other.attribution['ID'],
            DAMAGE,
            self.attribution['ID']))
        else:
            print('%s was attacked (%s) by %s' %(
            self.other.attribution['ID'],
            'MISS',
            self.attribution['ID']))


    def fight(self, other, heal, heal2):
        self.other = other
        while player1.check(player2) == True:
                player1.attack(player2)
                player1.healing(heal)
                print('%s have %s HP remining' %(self.other.attribution['ID'],
                self.other.attribution['HEALTH']))
                time.sleep(1)
                player2.attack(player1)
                player2.healing2(heal2)
                print('%s have %s HP remining' %(self.attribution['ID'],
                self.attribution['HEALTH']))
                time.sleep(1)

    def check(self, other):
        if self.attribution['HEALTH'] <= 0:
            print('%s was killed by %s' %(self.attribution['ID'],
            self.other.attribution['ID']))
            print("remaining %s's HP: %s" %(self.other.attribution['ID'],
            self.other.attribution['HEALTH']))
            return False
        elif self.other.attribution['HEALTH'] <= 0:
            print('%s was killed by %s' %(self.other.attribution['ID'],
            self.attribution['ID']))
            print("remaining %s's HP: %s" %(self.attribution['ID'],
            self.attribution['HEALTH']))
            return False
        else:
            return True

player1 = input('your name: ')
player2 = input('opponent name: ')
Health = int(input('your Health: '))
Health2 = int(input('opponent Health: '))

def Healstation_check():
    Healstation = int(input('you on a heal station? (1=yes,2=no): '))
    if Healstation == 1:
        return 3
    elif Healstation == 2:
        return 0
    else:
        return 0

def Healstation2_check():
    Healstation2 = int(input('opponent on a heal station? (1=yes,2=no): '))
    if Healstation2 == 1:
        return 3
    elif Healstation2 == 2:
        return 0
    else:
        return 0

heal = 1
heal2 = 1

heal = Healstation_check()
heal2 = Healstation2_check()

print(heal)
print(heal2)
time.sleep(2)
player1 = Character(player1, Health)
player2 = Character(player2, Health2)

player1.fight(player2, heal, heal2)
