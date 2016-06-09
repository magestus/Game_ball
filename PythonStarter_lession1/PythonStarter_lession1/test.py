# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


name = input ('Привет, как тебя зовут?')

age = input ('Сколько тебе лет?')
age = int (age)

weight = int (input ('Хорошо. И последний вопрос. Сколько в тебе килограммов?'))
print ('\nЕсли бы поэт Каммингс адресовал тебе письмо, он бы обратился к тебе так: ', name.upper())
called = name * 5
print ('\nЕсли бы маленький ребёнок решил привлечь твоё внимание',)
print ('он произнёс бы твоё имя так: ')
print (called)
second = age * 365 * 24 * 60 * 60
print ('\nТвой нынешний возраст - свыше' , second , 'секунд.')
moon_weight = weight / 6
print ('\nЗнаете ли вы, что на Луне вы весили бы всего' , moon_weight , 'кг?')
sun_weight = weight * 27.1
print ('А вот находясь на Солнце, вы бы весили' , sun_weight, 'кг (Но, увы, бла, бла'))
input ('\n\nНажмите enter чтобы выйти.')