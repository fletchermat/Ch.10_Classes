class Character():
    def __init__(self,name):
        self.name = name
    def fight(self):
        print("\"Lightsaber on!\" says "+self.name+".")

class Jedi(Character):
    def __init__(self,name,strength):
        super().__init__(name)
        self.strength = strength
    def fight(self):
        super().fight()
        print("\"Come to the light side! My strength is",self.strength,",\" says",self.name,".")

class Sith(Character):
    def __init__(self,name,my_apprentice):
        super().__init__(name)
        self.my_apprentice = my_apprentice
    def fight(self):
        print("\"Come to the Dark side!\" says",self.name,".")
        print("My apprentice is ",self.my_apprentice)
luke = Jedi("Luke Skywalker",100)
Darth = Sith("Darth Sideous","Darth Vader")
luke.fight()
Darth.fight()

