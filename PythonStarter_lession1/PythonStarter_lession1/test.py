# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


name = input ('������, ��� ���� �����?')

age = input ('������� ���� ���?')
age = int (age)

weight = int (input ('������. � ��������� ������. ������� � ���� �����������?'))
print ('\n���� �� ���� �������� ��������� ���� ������, �� �� ��������� � ���� ���: ', name.upper())
called = name * 5
print ('\n���� �� ��������� ������ ����� �������� ��� ��������',)
print ('�� ������� �� ��� ��� ���: ')
print (called)
second = age * 365 * 24 * 60 * 60
print ('\n���� �������� ������� - �����' , second , '������.')
moon_weight = weight / 6
print ('\n������ �� ��, ��� �� ���� �� ������ �� �����' , moon_weight , '��?')
sun_weight = weight * 27.1
print ('� ��� �������� �� ������, �� �� ������' , sun_weight, '�� (��, ���, ���, ���'))
input ('\n\n������� enter ����� �����.')