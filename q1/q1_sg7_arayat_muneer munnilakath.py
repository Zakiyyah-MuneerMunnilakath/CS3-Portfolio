class Glassware:
    def __init__(self, name):
        self.name = name

class Beaker(Glassware):
    def __init__(self, name):
        super().__init__(name)

class Tray:
    def __init__(self):
        self.beakers = [Beaker("Beaker 1"), Beaker("Beaker 2"), Beaker("Beaker 3"),
                        Beaker("Beaker 4"), Beaker("Beaker 5")]

tray = Tray()
print(tray.beakers[0].name)
del tray
