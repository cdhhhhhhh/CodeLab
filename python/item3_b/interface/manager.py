from python.item3_b.interface import db
from python.item3_b.interface import common



def register_interface(name, password):
    obj = {'username': name, 'password': password}
    db.save('manager', obj, name)
    common.get_logger(__name__).info('注册成功')
