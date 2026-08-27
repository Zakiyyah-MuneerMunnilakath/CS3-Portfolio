class Hero:
    def __init__(self,name, hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self, damage):
        self.hp = self.hp - damage

arthur = Hero("Arthur")
morgana = Hero("Morgana")

arthur.take_damage(10)

print(f"Arthur hp: {arthur.hp}")
print(f"Morgana hp: {morgana.hp}")
