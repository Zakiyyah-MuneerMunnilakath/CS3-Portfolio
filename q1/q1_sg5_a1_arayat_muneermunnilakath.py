class Hero:
    def __init__(self,name, hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self, damage):
        self.hp = self.hp - damage
        print(f"{name} has {s} hp left.")

arthur = Hero("Arthur")
morgana = Hero("Morgana") 
