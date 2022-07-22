#!/usr/bin/env python
#_*_ coding: utf8 _*_

class Color:

    @classmethod 
    def red(cls):
        return '\033[91m'
    
    @classmethod
    def yellow(cls):
        return '\033[93m'

    @classmethod
    def green(cls):
        return '\033[92m'

    @classmethod
    def purpleLigth(cls):
        return '\033[94m'

    @classmethod
    def purple(cls):
        return '\033[95m'

    @classmethod
    def ligthBlue(cls):
        return '\033[96m'

    @classmethod
    def ligthGray(cls):
        return '\033[97m'

    @classmethod
    def black(cls):
        return '\033[98m'

    @classmethod
    def endColor(cls):
        return '\033[00m'



if __name__=='__main__':

    print(f'{Color.ligthBlue()} hola mundo {Color.endColor()}')
