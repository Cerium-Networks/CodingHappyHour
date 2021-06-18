import random

class Character():

    def CalculateAttackDamage(self):
        return random.randint(1, self.Attack) * self.Weapon

    def __init__(self, name, hp, attack, defence, luck, exp = 0, weapon = None, shield = None):

        self.Name = name
        self.HP = hp
        self.Attack = attack
        self.Defence = defence
        self.Luck = luck
        self.Exp = exp

        self.Weapon = weapon
        self.Shield = shield



def main():
    Hero = Character("Nich", 100, 10, 10, 3, weapon=2.3)
    BadGuy = Character("Zach", 80, 8, 8, 5, weapon=2.6)

    while(BadGuy.HP > 0 and Hero.HP > 0):
        BadGuy.HP -= Hero.CalculateAttackDamage()
        Hero.HP -= BadGuy.CalculateAttackDamage()

    if(BadGuy.HP > 0):
        print(BadGuy.Name + " won the fight")
    elif(Hero.HP > 0):
        print(Hero.Name + " won the fight")
    else:
        print("it was a draw")

main()
