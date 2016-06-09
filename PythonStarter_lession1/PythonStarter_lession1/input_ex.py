# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


string = input('Enter a string: ')
print('You have entered','{',string,'}', sep='')


input()

n = int(input('first number: '))
m = int(input('Second number: '))
print('{} + {} = {}'.format(n, m, n+m))