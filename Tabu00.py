#!/usr/bin/env python
# encoding: utf-8
'''
@author: 85770
@contact: 14290385@outlook.com
@file: hi.py
@time: 2019/3/11 14:21
'''
import random
import matplotlib.pyplot as plt
import numpy as np

print('hi')
# city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41,
#           44, 4]
# city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26,
#           35, 50]
# 坐标随机生成
city_randomX = []
city_randomY = []
cityNum = int(input('enter the num of city:'))
Tabu_list = []
Tabu_limitLength = 50


class city:

    def __init__(self, x_l, y_l):
        self.x_localtion = x_l
        self.y_localtion = y_l


class Distance():
    def __init__(self, x1, y1, x2, y2):
        self.distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


for i in range(cityNum):
    city_randomX.append(random.randint(0, 200))
    city_randomY.append(random.randint(0, 200))
for x, y, i in zip(city_randomX, city_randomY, range(cityNum)):
    exec('city{}=city(x, y)'.format(i))
    exec('print(city{}.x_localtion , city{}.y_localtion)'.format(i, i))

for i in range(cityNum):
    x = eval('city{}.x_localtion'.format(i))
    y = eval('city{}.y_localtion'.format(i))
    plt.plot(x, y, 'ro')
plt.show()
init_list = np.arange(cityNum)

print(init_list)
for i in range(10):
    np.random.shuffle(init_list)  # 随机排列
    print(init_list)

# city1 = city(10, 32)
# city2 = city(235, 12)
# distance1 = Distance(city1.x_localtion, city1.y_localtion, city2.x_localtion, city2.y_localtion)
# print(distance1.distance)
