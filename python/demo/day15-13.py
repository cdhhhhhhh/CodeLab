import abc


class Pet:
    def __init__(self, name):
        self.__name = name

    @abc.abstractmethod
    def eat(self):
        pass

    def get_name(self):
        return self.__name


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.__type = 'cat'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        self.__type = x

    def eat(self):
        print(self.get_name()+'吃喵粮')


class Pig(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.__type = 'pig'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        self.__type = x

    def eat(self):
        print(self.get_name()+'吃猪粮')


class Dog(Pet):

    def __init__(self, name):
        super().__init__(name)
        self.__type = 'dog'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        self.__type = x

    def eat(self):
        print(self.get_name()+'吃狗粮')


class Master:

    def __init__(self, name, pet):
        self.__name = name
        self.__pet = pet

    def feed(self):
        print(self.__name+'喂'+self.__pet.get_name())
        print(self.__pet.type+'品种的'+self.__pet.get_name())
        self.__pet.eat()


pet1 = Dog('ddd')
pet2 = Cat('ccc')
pet3 = Pig('ppp')

master1 = Master('master1', pet1)
master2 = Master('master2', pet2)
master3 = Master('master3', pet3)

master1.feed()