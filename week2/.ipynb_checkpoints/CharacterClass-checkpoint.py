import random as rand
import numpy as np
class abilities:
    ''''''
    def __init__(self):
        self.str = 0
        self.dex = 0
        self.con = 0
        self.wis = 0
        self.cha = 0
        self.int = 0


    def roll_ability(self):
        """ Calulate ability score returns a value between 3 and 18.
                We use a list to hold the data and append each dice.
                We then drop the lowest and return the sum

            """
        d6_list = []
        for dice in range(0, 4):
            d6_list.append(rand.randint(1, 6))
        d6_list.pop(np.argmin(d6_list))
        return np.sum(d6_list)

    def calculate_modifier(modifiers , abilities):
        for s in dir(modifiers):
            if not s.startswith('__'):
                modifiers[s] = (abilities.str - 10) // 2
        return modifiers

class character:

    """
    This is a character class. Calling this class will initialize all the information we need. """



    def __init__(self, name, class_name, level, race, hitdice, age, proficiency):
        self.name=name
        self.class_name= class_name
        self.level= level
        self.race= race
        self.hitDice = hitdice

        self.age = age
        self.proficiency = proficiency
        self.abilityScores = abilities()
        self.abilityScores.str = abilities.roll_ability(self)
        self.abilityScores.dex = abilities.roll_ability(self)
        self.abilityScores.con = abilities.roll_ability(self)
        self.abilityScores.wis = abilities.roll_ability(self)
        self.abilityScores.int = abilities.roll_ability(self)
        self.abilityScores.cha = abilities.roll_ability(self)
        self.abilityModifiers = abilities()
        self.abilityModifiers.str = (self.abilityScores.str - 10) // 2
        self.abilityModifiers.dex = (self.abilityScores.dex - 10) // 2
        self.abilityModifiers.con = (self.abilityScores.con - 10) // 2
        self.abilityModifiers.wis = (self.abilityScores.wis - 10) // 2
        self.abilityModifiers.int = (self.abilityScores.int - 10) // 2
        self.abilityModifiers.cha = (self.abilityScores.cha - 10) // 2
        self.hp = 0
        self.hp = hitdice + self.abilityModifiers.con
        self.hp += self.add_HP(hp = self.hp, levels = (level ), con=self.abilityModifiers.con)
        self.current_hp = self.hp
        self.AC = 10 + self.abilityModifiers.dex
        self.Has_Healing_potion = True
    def add_levels(self, levels):
        self.level += levels
        self.hp = self.add_HP(self.hp, levels=levels, con=self.abilityModifiers.con)
    #
    def melee_attack(self, attack_Modifier, damage_die):
        attack_roll = rand.randint(1, 20) + attack_Modifier + self.proficiency
        damage = rand.randint(1, damage_die) + attack_Modifier
        return attack_roll, damage

    def add_HP(self, hp, levels, con):
        for level in range(0, levels):
            hp += rand.randint(1, 10) + con

        return hp


if __name__ =="__main__":
    laern = (character(name = "Leeroy Jenkins",
race = "elf",
level = 1,
age = 19,
class_name = "Fighter",
hitdice = 10, proficiency=3))
    print(laern.abilityScores.str)
    laern.add_levels(3)
    print(laern.melee_attack(laern.abilityModifiers.str, 8))
