#!/usr/bin/env python
# encoding: utf-8
'''
@author: 85770
@contact: 14290385@outlook.com
@file: cityData.py
@time: 2019/4/3 16:54
'''
city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41,
          44, 4]
city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26,
          35, 50]
cityNum = 30


class City:

    def __init__(self, x_l, y_l):
        self.x_localtion = x_l
        self.y_localtion = y_l


for x, y, i in zip(city_x, city_y, range(cityNum)):
    exec('city{}=City(x, y)'.format(i))
    print('city{}'.format(i), eval('city{}.x_localtion'.format(i)), eval('city{}.y_localtion'.format(i)))
    # exec('print(city{}.x_localtion , city{}.y_localtion)'.format(i, i))
