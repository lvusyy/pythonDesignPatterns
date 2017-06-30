class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
        # 相互作用

    def interact_with(self, obstacle):
        # 青蛙 遇到                                #障碍
        print('{} the Frog encounters {} and {} !'.format(self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------Frog World-----------'
        # 字符

    def make_character(self):
        return Frog(self.player_name)
        # 障碍

    def make_obstacle(self):
        return Bug()
        # 巫师/男巫


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the  Wizard battles aginst {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------Wizard World--------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def Validate_age(name):
    try:
        age = input('Welcom {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid,please try again...".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. what's you name? ")
    vaild_input = False
    while not vaild_input:
        vaild_input, age = Validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
