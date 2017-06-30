from  enum import Enum
import time

# 进展        队列     准备        饼
PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')

'''
#生成的内容类似这样
classs PizzaProgress(Enum):
queued=1
preparation=2
baking=3
ready=4
'''
# 面团    thin 瘦 薄 thick 厚
PizzaDough = Enum('PizzaDough', 'thin thick')
# 披萨酱
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
# 披萨配料      奶酪         双层奶酪            培根 火腿     蘑菇    红色洋葱   牛至
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3  # 秒


class Pizza:
    def __init__(self, name):
        self.name = name  # pizza名字
        self.dough = None  # 面团
        self.sauce = None  # 酱
        self.topping = []  # 配料

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of you {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margariata')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('add the tomato sauce to you margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella,oregano) to you margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella,oregno)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking you margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('you margarita is ready')


class CreamyBaconBuilder:
    def __init__(self):  # 奶油 培根
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7  # 秒

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the creme fraiche suce to you creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme fraiche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella,bacon ham,hushrooms,red onion,oregano) to you creamy bacon')
        self.pizza.topping.append([t for t in (
            PizzaTopping.mozzarella, PizzaTopping.bacon, PizzaTopping.ham, PizzaTopping.mushrooms,
            PizzaTopping.red_onion,
            PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella,bacon,hum,mushrooms,red onion,oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking you creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input("what pizaa would you like,[m]argarita or [c]reamy bacon?")
        builder = builders[pizza_style]()
        # valid_input=True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are valiable')
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy you {}!'.format(pizza))


if __name__ == '__main__':
    main()
