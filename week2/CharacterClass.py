import random as rand
import numpy as np


class abilities:

    def __init__(self):
        """
        used to house ability variables
        @param str: strength variable
        @param dex: dexterity variable
        @param con: constitution variable
        @param wis: wisdom variable
        @param cha: charisma variable
        @param int: intelligence variable
        """
        self.str = self.Ability()
        self.dex = self.Ability()
        self.con = self.Ability()
        self.wis = self.Ability()
        self.cha = self.Ability()
        self.int = self.Ability()

    class Ability:
        """Sub class used to house the score and the modifier for each ability.
        Two Functions:
        @param roll_ability: rolls ability score using 4d6 drop lowest
        @param calculate_modifier; function to calculate ability score modifier.
        """
        def __init__(self):
            self.score = 0


        def roll_ability(self):
            """ Calulate ability score returns a value between 3 and 18.
                    We use a list to hold the data and append each dice.
                    We then drop the lowest and return the sum

                """
            d6_list = []
            for dice in range(0, 4):
                d6_list.append(rand.randint(1, 6))
            d6_list.pop(np.argmin(d6_list))
            self.score = np.sum(d6_list)
            self.calculate_modifier()

        def calculate_modifier(self):
            self.modifier = (self.score - 10) // 2


class character:
    """
    This is a character class. Calling this class will initialize all the information we need.

    """

    def __init__(self, name, class_name, level, race, hitdice, age, proficiency):
        self.name = name
        self.class_name = class_name
        self.level = level
        self.race = race
        self.hitDice = hitdice

        self.age = age
        self.proficiency = proficiency
        self.abilityScores = abilities()
        self.abilityScores.str.roll_ability()
        self.abilityScores.dex.roll_ability()
        self.abilityScores.con.roll_ability()
        self.abilityScores.wis.roll_ability()
        self.abilityScores.int.roll_ability()
        self.abilityScores.cha.roll_ability()
        self.hp = 0
        self.hp = hitdice + self.abilityScores.con.modifier
        self.hp += self.add_HP(hp=self.hp, levels=(level), con=self.abilityScores.con.modifier)
        self.current_hp = self.hp
        self.AC = 10 + self.abilityScores.dex.modifier
        self.Has_Healing_potion = rand.choice([True, False])

    def add_levels(self, levels):
        self.level += levels
        self.hp = self.add_HP(self.hp, levels=levels, con=self.abilityScores.con.modifier)

    #
    def melee_attack(self, attack_Modifier, damage_die):
        attack_roll = rand.randint(1, 20) + attack_Modifier + self.proficiency
        damage = rand.randint(1, damage_die) + attack_Modifier
        return attack_roll, damage

    def add_HP(self, hp, levels, con):
        for level in range(0, levels):
            hp += rand.randint(1, 10) + con

        return hp


if __name__ == "__main__":
    laern = (character(name="Leeroy Jenkins",
                       race="elf",
                       level=1,
                       age=19,
                       class_name="Fighter",
                       hitdice=10, proficiency=3))
    print(laern.abilityScores.str)
    laern.add_levels(3)
    print(laern.melee_attack(laern.abilityScores.str.modifier, 8))
