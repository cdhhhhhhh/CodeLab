#元类
class CarMate(type):
    def __init__(self, class_name, class_bases, class_dic):
        super(CarMate, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):

        obj = object.__new__(self)
        self.__init__(obj, *args, **kwargs)

        if not(hasattr(obj, 'number') and hasattr(obj, 'date') and hasattr(obj, 'capacity')):
            raise TypeError('需填写 date number capacity 参数')
        return obj


class Car(object, metaclass=CarMate):

    def __init__(self, date, number, capacity):
        self.date = date
        self.number = number
        self.capacity = capacity

    def info(self):
        print(self.date, self.capacity, self.number)

bus = Car( 1023, 20, 30)

bus.info()