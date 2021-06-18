import random


class Character():
    

    def GenerateRandomStats(Exp):

        remainingExp = Exp

        attack = random.randint(2,Exp/2) - 1
        remainingExp -= attack

        defense = random.randint(2,Exp/2) - 1
        remainingExp -= defense

        hitpoints = (remainingExp + 2) * 10

        luck = random.randint(0, 5)

        return {"atk":attack, "def":defense, "hp":hitpoints, "luck":luck}


    def CalculateCritAndDamage(self, damage):
        critChance = self.Weapon.Critchance
        critChance += self.CombatStats['luck']

        if(random.randint(0,100) < critChance):
            return damage * 2
        elif(random.randint(0, 100) < 5):
            return damage // 2
        else:
            return damage


    def CalculateAttackDamage(self):
        if self.Weapon is None:
            weaponDamage = random.randint(0, self.CombatStats['atk'])
        else:
            weaponDamage = int(random.randint(0, self.CombatStats['atk']) * self.Weapon.Damage * 0.1) 

        finalDamage = Character.CalculateCritAndDamage(weaponDamage)

        return finalDamage


    def __init__(self, Name="Nich", Exp=20):
        self.Name = Name
        self.Weapon = None
        self.Shield = None

        self.CombatStats = Character.GenerateRandomStats(Exp)
