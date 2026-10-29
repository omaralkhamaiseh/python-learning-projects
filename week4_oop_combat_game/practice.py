class Player:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def take_damage(self,damage_ammount):
        self.health=self.health-damage_ammount
        print(f"{self.name} took {damage_ammount} damage! HP now is {self.health}")
player1=Player("Omar",100,25)
player1.take_damage(50)
print(f"{player1.name} your health is {player1.health} and your attack power is {player1.attack_power}")