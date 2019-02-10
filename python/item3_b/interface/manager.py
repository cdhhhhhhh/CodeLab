from python.item3_b.interface import db


def register_interface(name, password):
    obj = {'username': name, 'password': password}
    db.save('manager', obj, name)
