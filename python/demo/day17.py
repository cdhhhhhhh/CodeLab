class Interger():
    def __init__(self,number):
        self.number = number

    def input(self):
        if type(self.number) == str:
            raise SlopOverError('invalid literal for init() with base 10', self.number)
        if not type(self.number) == self.number:
            print('数字不合法重新输入')
            self.number = input('输入')
            self.input()
        if not self.VerifySlopOver(self.number):
            raise SlopOverError('ErrorMsg', str(self.number) + '-越界')

    def VerifySlopOver(self, number):
        return -2147483648 < number < 2147483648


class SlopOverError(BaseException):
    def __init__(self, number, message):
        self.number = number
        self.message = message

    def __str__(self):
        return '<'+self.message+str(self.number)+'>'


Interger([1,2,3]).input()