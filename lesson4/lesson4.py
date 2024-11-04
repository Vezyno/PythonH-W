s = input('Введите строку: \n')
flag = True
string  = ''
for i in range (len(s)):
  if s[i]!= ' ':
    string +=s[i]
print(string)
for i in range(len(s)//2):
  if string[i] != string[-1-i]:
    flag = False
    break
print('Палиндром') if flag else print('Не палиндром')


import numpy as np
# l = np.array([i*i for i in range(10)])
l = [i*i for i in range(10)]
print(max(l))


# from random import randint
from random import *
# import random
l = [randint(0, 1000) for x in range(10)]
print(l)


my_string = input()
letter = input()
symbols = [r'(', r' ', ''] #Можно добавить еще...
res = 0
for symbol in symbols:
  if my_string.find(symbol + letter.lower()):
      res += 1
print(res)