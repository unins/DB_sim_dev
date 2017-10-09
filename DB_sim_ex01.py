import random, time

class Character(object):
    def __init__(self, user_id, health, heal_station):  # GET : ID, HEALTH
        self.attribution = {
            'ID' : user_id,
            'HEALTH' : health,
            'HEAL' : heal_station, }

    def get_heal(self, heal=3):        # IN: 'int' / OUT: 'int'
        if heal:
            self.attribution['HEALTH'] += heal
        else:
            pass

        remain_health = self.attribution['HEALTH']
        return remain_health

    def attack(self, other):        # IN: OBJECT / OUT: 'int', 'int'
        self.other = other

        # ---- NORMAL DEMAGE : [0, 1, 2, 3, 4]
        if random.randint(0,10) in [0, 1, 2, 3, 4]:
            DAMAGE = random.randint(2,10)
            self.METHOD = 'NORMAL'
            self.other.attribution['HEALTH'] -= DAMAGE

        # ---- SPECIAL DEMAGE : [5, 6, 7]
        elif random.randint(0,10) in [5, 6, 7]:
            DAMAGE = random.randint(20,35)
            self.METHOD = 'CRIRICAL'
            self.other.attribution['HEALTH'] -= DAMAGE

        # ---- MISS BLOW : [8, 9]
        else:
            DAMAGE = 0
            self.METHOD = 'MISS'

        return (DAMAGE, self.other.attribution['HEALTH'], self.METHOD)

    def is_dead(self):              # IN: - / OUT : 'bool' = True/False
        if self.attribution['HEALTH'] <= 0:
            return True
        else:
            return False

    def show_status(self):          # self status report
        print("%s's health = %s remain... "% (
            self.attribution['ID'],
            self.attribution['HEALTH']))


# ---- INPUT OBJECT PARAMETER
PLAYER_1, PLAYER_2 = input('your name: '), input('opponent name: ')
HEALTH_1, HEALTH_2 = int(input('your Health: ')), int(input('opponent Health: '))
HEAL_1, HEAL_2 = int(input('you on a heal station? (1=yes,2=no): ')),\
    int(input('opponent on a heal station? (1=yes,2=no): '))
print('__'*30)

# ---- SET OBJECTS
YOU = Character(PLAYER_1, HEALTH_1, HEAL_1)
OPP = Character(PLAYER_2, HEALTH_2, HEAL_2)

def heal_self(obj, heal_point):
    remain_health = obj.get_heal(heal_point)
    print('%s is healed by (%s) points,.. health %s remains...' %(
        obj.attribution['ID'],
        heal_point, remain_health ))
    print()
    return remain_health

def fight(you, opp):        # IN: OBJECT, OBJECT
    [damage, remain_health, attack_method] = you.attack(opp)
    print("'%s' attacks [%s] '%s' (-%s) / health %s remains..." %(
        you.attribution['ID'],
        attack_method,
        opp.attribution['ID'],
        damage, remain_health,))
    opp.show_status()
    time.sleep(0.2)

def final_score():
    print('__'*30)
    YOU.show_status()
    OPP.show_status()
    print('__'*30)


while True:
    # ---- ATTACK ----------------------
    if YOU.is_dead():
        print("%s is killed" %YOU.attribution['ID'] )
        final_score()
        break

    fight(YOU, OPP)

    if YOU.attribution['HEAL']:
        heal_self(YOU, heal_point=random.choice([1, 2, 3, 4, 5]))
        # Random healing +1 ~ +5

    # ---- DEFENSE ----------------------
    if OPP.is_dead():
        print("%s is killed" %OPP.attribution['ID'] )
        final_score()
        break

    fight(OPP, YOU)

    if OPP.attribution['HEAL']:
        heal_self(OPP, heal_point=random.choice([1, 2, 3, 4, 5]))
