#!/usr/bin/env python
# coding=utf-8

class Brid:
    fly = "whirring"
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('aaah....')
            self.hungry = False
        else:
            print('no, thanks')

class Apodidae(Brid):
    def __init__(self):
        super(Apodidae,self).__init__()
        self.sound = 'squawk!'
    def sing(self):
        print(self.sound)


swift = Apodidae()
swift.fly
swift.eat()
swift.eat()
swift.sing()
