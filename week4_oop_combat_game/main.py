import random
import time 
class Player:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def attack(self,target):
         damage_dealt=random.randint(self.attack_power-5,self.attack_power+5)
         crit_roll=random.randint(1,100)
         if crit_roll<=20:
              damage_dealt=damage_dealt*2
              print(f"💥 CRITICAL HIT! {self.name} obliterated {target.name} for {damage_dealt} damage!")
         else:
              print(f"{self.name} attacked {target.name} for {damage_dealt} damage!")     
         target.health=target.health-damage_dealt
         print(f"{target.name} has {target.health} HP left.")
    def heal(self,heal_amount):
          self.health=self.health+heal_amount
          print(f"{self.name} healed for {heal_amount} HP! Health is now {self.health}.")
class Enemy:
     def __init__(self,name,health,attack_power):
            self.name=name
            self.health=health
            self.attack_power=attack_power 
     def attack(self,target):
             damage_dealt=random.randint(self.attack_power-5,self.attack_power+5)
             target.health=target.health-damage_dealt
             print(f"{self.name} attacked {target.name} for {damage_dealt} damage! {target.name} has {target.health} HP left.")            
hero=Player("Omar",100,25)
boss=Enemy("Genichiro",150,15)
while True:
      print("\n--- COMBAT MENU ---")
      print("1. Attack")
      print("2. Heal")
      print("3. Run")
      choice = int(input("Make your move (1/2/3): "))
      if choice == 1:
            hero.attack(boss)
            time.sleep(1)
            if boss.health > 0:
                boss.attack(hero)
                time.sleep(1)
      elif choice ==2:
            hero.heal(15)  
            time.sleep(1)
            boss.attack(hero)
            time.sleep(1)
      elif choice ==3:
            break
      if hero.health <= 0 or boss.health <= 0:
        print("The battle is over!")
        break
            
                  