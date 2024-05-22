import random

# # Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health 
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
    
##Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {self.damage} points"
        else:
            return f"{self.name} has died in act of combat"

# # Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"     

# # Davicente

# class War():
#     def __init__(self):
#         self.vikingArmy = []
#         self.saxonArmy = []

#     def addViking(self, viking):
#         self.vikingArmy.append(viking)
    
#     def addSaxon(self, saxon):
#         self.saxonArmy.append(saxon)
    
#     def vikingAttack(self):
#         result = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)
#     for saxon in self.saxonArmy:
#         if saxon.health <= 0:
#             self.saxonArmy.remove(saxon)
#     return result

#     def saxonAttack(self):
#         result2 = random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)
#     for viking in self.vikingArmy:
#         if viking.health <= 0:
#             self.vikingArmy.remove(viking)
#     return result

#     def showStatus(self):
#         if not self.saxonArmy:
#             return "Vikings have won the war of the century!"
        
#         #if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
#         if not self.vikingArmy:
#             return "Saxons have fought for their lives and survive another day..."
        
#         #if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
#         if self.saxonArmy and self.vikingArmy:
#             return "Vikings and Saxons are still in the thick of battle."
    #pass

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


