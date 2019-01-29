class Hero:
    def __init__(self, name, lvl, hp, Q_hurt, W_hurt, E_hurt):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.Q_hurt = Q_hurt
        self.W_hurt = W_hurt
        self.E_hurt = E_hurt

    def attack(self, obj, skill):
        if self.hp > 0:
            obj.hp -= self.__dict__[skill]
            print('%s攻击%s 技能伤害%s当前血量%s'%(self.name, obj.name, self.__dict__[skill], obj.hp))
        else:
            print('you die')


foo = Hero('foo', 5, 100, 10, 11, 12)
bar = Hero('bar', 4, 100, 22, 12, 22)
foo.attack(bar, 'Q_hurt')
foo.attack(bar, 'Q_hurt')
bar.attack(foo, 'W_hurt')
bar.attack(foo, 'W_hurt')




