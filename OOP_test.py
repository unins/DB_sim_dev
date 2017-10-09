import random
import os
import time
""" ---------------------------------- CHAPTER.02 LESSON.07--- class OOP Drill
 OOP drill - Game Charactor
 (1) class =  __init__, ask_intro, attack, is_dead
 (2) outer = clear, pop_menu, get_attack(msg), get_dead(msg)
"""

MESSAGE = '''
 \t  +__+__+__+__+__+__+__+__+__+__+__+
 %s
 \t  +^^+^^+^^+^^+^^+^^+^^+^^+^^+^^+^^'''

class Charactor(object):
    def __init__(self, name):
        self.attribution = {
            'NAME': name,
            'TRIBE': 'Human',
            'LIFE': 100,
            'DEMAGE' : 10,
            'WEAPON' : 'FIST'
        }

    def ask_intro(self, other):     # IN : other = OBJECT
        self.other = other

        self.i_message = "%s : 'Who are you?..', -- '%s' asked.. --" %(
            self.attribution['NAME'],
            self.attribution['NAME'])

        self.u_message = "\t\tHi~! My name is '%s' ...\n\t\tI'm a '%s'" %(
            self.other.attribution['NAME'],
            self.other.attribution['TRIBE'])

        print(self.i_message, "\n\n\n", MESSAGE % self.u_message)

    def attack(self, other):        # IN : other = OBJECT
        self.other = other          # object

        if random.randint(0, 10) in [0, 3, 7, 9]:
            print(" Attack was *** FAILED *** ")
        else:
            self.added_attack = (self.attribution['DEMAGE'] + random.choice([-1, 1, 2, 3])*5)
            self.other.attribution['LIFE'] -= self.added_attack

            print(" '%s' is attacked (-%s) by '%s', Life remains %s" %(
                self.other.attribution['NAME'],
                self.added_attack,
                self.attribution['NAME'],
                self.other.attribution['LIFE']))

    def is_dead(self):              # Out = BOOL
        if self.attribution['LIFE'] <= 0:
            return True
        else:
            return False


class Worrior(Charactor):
    def __init__(self, name):
        self.attribution = {
            'NAME': name,
            'TRIBE': 'Worrior',
            'LIFE': 300,
            'DEMAGE' : 50,
            'WEAPON' : 'AXE'
        }

    def special_attack(self):
        pass


def clear():
    time.sleep(1)
    os.system('cls')

def pop_menu():
    print('__'*30)
    menu_list = "(1) ASK   (2) ATTACK   (3) CHAINLY-ATTACK : 5-Combo   (4) Clear"
    action = input("select menu \n  %s\n" % menu_list)
    print('..'*30)
    return action

def get_attack(me, other, n):  # In : OBJECTS
    for i in range(n):
        print("attack (%s) = "%(i+1), end="")
        me.attack(other)
        print()

def get_dead(target):   # In: OBJECT
    print('%s is DEAD...'% target.attribution['NAME'])
    print('LIFE = %s' % target.attribution['LIFE'])



MINT = Charactor('MiNt')
PEPPER = Worrior('PePpEr')

print("\n\nMINT meets PEPPER... \n\n")

while True:
    action = pop_menu()

    try:
        if action == '1':
            MINT.ask_intro(PEPPER)
            print()

        elif action == '2':
            if PEPPER.is_dead() != True:
                get_attack(MINT, PEPPER, 1)
            else:
                get_dead(PEPPER)

        elif action == '3':
            for n in range(5):
                if PEPPER.is_dead():
                    get_dead(PEPPER)
                    break
                else:
                    get_attack(MINT, PEPPER, 1)
        else:
            clear()
    except KeyError as e:
        pass
