heroClasses = {
    'Mago': {'Atk': 'magia'},
    'Guerreiro': {'Atk': 'espada'},
    'Monge': {'Atk': 'artes marciais'},
    'Ninja': {'Atk': 'shuriken'}
}
class hero:
    def __init__(self, name, age, heroClass):
        self.name = name
        self.age = age
        self.myHeroClass = myHeroClass

    def heroAttack(self):
        if self.myHeroClass in heroClasses:
            return heroClasses[self.myHeroClass]['Atk']
        else: 
            return "Classe inexistente"

name = "Invincible"
age = "18"
myHeroClass = "Monge"

my_hero = hero(name, age, myHeroClass)
tipo_ataque = my_hero.heroAttack()

print(f"O {my_hero.myHeroClass} atacou usando {tipo_ataque}.")