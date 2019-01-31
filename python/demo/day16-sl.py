#单例模式
#类方式
setting = {'IP':'xxxxxx','PORT':'xxx'}


class SlingMode1:
    __instance = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def create_singleton(cls):
        if not cls.__instance:
            obj = cls(setting['IP'], setting['PORT'])
            cls.__instance = obj

        return cls.__instance


obj1 = SlingMode1.create_singleton()
obj2 = SlingMode1.create_singleton()
print(obj1 is obj2 )

#元类方式
class SlingModeMeta(type):

    __instance = None

    def __init__(self, class_name, class_bases, class_dic):
        super(SlingModeMeta, self).__init__(class_name, class_bases, class_dic)

    @classmethod
    def create_singleton(cls):
        if not cls.__instance:
            cls.__instance =setting

        return cls.__instance


class SlingMode2(metaclass=SlingModeMeta):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


obj3 = SlingMode2.create_singleton()
obj4 = SlingMode2.create_singleton()
print(obj3 is obj4)

#模块
#装饰器


