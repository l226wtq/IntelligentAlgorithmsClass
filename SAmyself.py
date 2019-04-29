#!/usr/bin/env python
# encoding: utf-8
'''
@author: 85770
@contact: 14290385@outlook.com
@file: opencv.py
@time: 2019/4/15 0015 10:09
'''
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import copy

city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41,
          44, 4]
city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26,
          35, 50]
cityNum = city_y.__len__()
initT = 100 * cityNum
attenuationK = 0.99
markovL = 100


class citySolve(object):

    def __init__(self, cityList):
        self.cityList = cityList
        self.cityDistance = 0
        self.distance()
        self.Tnow = initT
        self.drawPlot()

    def distance(self):
        tempdistance = 0
        list = self.cityList
        for i, j in zip(range(cityNum), range(cityNum)):
            if j != cityNum - 1:
                tempdistance += ((city_x[list[i]] - city_x[list[i + 1]]) ** 2 + (
                        city_y[list[i]] - city_y[list[i + 1]]) ** 2) ** (1 / 2)
            else:
                tempdistance += ((city_x[list[i]] - city_x[0]) ** 2 + (city_y[list[i]] - city_y[0]) ** 2) ** (1 / 2)
        self.cityDistance = tempdistance

    def drawPlot(self):
        plt.clf()
        list = self.cityList
        for i, j in zip(range(cityNum), range(cityNum)):
            # x = eval('city{}.x_localtion'.format(self.solveList[i]))
            # y = eval('city{}.y_localtion'.format(self.solveList[i]))
            x = city_x[list[j]]
            y = city_y[list[j]]
            plt.scatter(x, y, c='b')
            if i == 0:
                x0 = x
                y0 = y
            else:
                x2 = city_x[list[j - 1]]
                y2 = city_y[list[j - 1]]
                plt.plot([x, x2], [y, y2], c='r')
                if i == cityNum - 1:
                    plt.plot([x, x0], [y, y0], c='r')  # 忽略编译器错误
        plt.title("T:%s,distance:%s" % (self.Tnow, self.cityDistance))
        plt.pause(0.0000000001)


class SA(object):
    def __init__(self, tempObject, Tmin, temp1, initT):
        self.Tmin = Tmin
        self.attenuationK = temp1
        self.Tnow = initT
        self.tempObject = tempObject
        self.solve()

    def solve(self):
        flag = 1
        while (self.Tnow >= self.Tmin):
            # self.Tnow *= self.attenuationK
            # print(self.tempObject.cityList)
            np.random.shuffle(self.tempObject.cityList)
            # print(self.tempObject.cityList)
            if flag == 1:
                beforeDistance = self.tempObject.cityDistance
            self.tempObject.distance()
            deltaE = self.tempObject.cityDistance - beforeDistance
            if (deltaE >= 0):
                Metropolis = math.exp(-deltaE / self.Tnow)
                if (Metropolis > random.random()):  # 接受新解
                    print(beforeDistance, self.Tnow, '接受新解', Metropolis, self.tempObject.cityDistance)
                    # self.tempObject.drawPlot()
                    flag = 1
                else:  # 不接受新解
                    print(beforeDistance, self.Tnow, Metropolis, '不接受新解', self.tempObject.cityDistance)
                    flag = 0
                    # continue

            else:  # 贪婪结果
                print(self.Tnow, '贪婪', self.tempObject.cityDistance)
                flag = 1
                # self.tempObject.drawPlot()
            self.Tnow *= self.attenuationK  # 降温
            self.tempObject.Tnow = self.Tnow


if __name__ == '__main__':
    initList = np.arange(cityNum)
    np.random.shuffle(initList)  # 初始解
    citySolveInit = citySolve(initList)
    saObject = SA(citySolveInit, 0.1, attenuationK, initT)
