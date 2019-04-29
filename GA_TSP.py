#!/usr/bin/env python
# encoding: utf-8
'''
@author: 85770
@contact: 14290385@outlook.com
@file: opencv.py
@time: 2019/4/29 0029 10:35
'''
import numpy as np
import copy

city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41,
          44, 4]
city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26,
          35, 50]
cityNum = city_y.__len__()
population = 50


class citySolve(object):

    def __init__(self, cityList):
        self.cityList = copy.copy(cityList)
        self.cityDistance = self.distance(self.cityList)

    def distance(self, list):
        tempdistance = 0
        # list = self.cityList
        for i, j in zip(range(cityNum), range(cityNum)):
            if j != cityNum - 1:
                tempdistance += ((city_x[list[i]] - city_x[list[i + 1]]) ** 2 + (
                        city_y[list[i]] - city_y[list[i + 1]]) ** 2) ** (1 / 2)
            else:
                tempdistance += ((city_x[list[i]] - city_x[0]) ** 2 + (city_y[list[i]] - city_y[0]) ** 2) ** (1 / 2)
        return tempdistance


def createInitPopulation(list):  # 生成初始种群
    initPopulation = []
    for i in range(population):
        np.random.shuffle(list)
        initPopulation.append(citySolve(list))
    return initPopulation


def selectPopulation(Population):
    Sum = 0
    fitness, cumulativeFitness = [], []
    selectRandom = np.random.rand()
    for i in Population:
        Sum += i.cityDistance
    for k in Population:
        fitness.append((1 - k.cityDistance / Sum) / (population - 1))  # 归一化的适应度
    for j in range(population):
        Sum2 = 0
        for l in fitness[:j + 1]:
            Sum2 += l
        cumulativeFitness.append(Sum2)
    for m in cumulativeFitness:
        if m > selectRandom:
            print(m)
            break
    pass


if __name__ == '__main__':
    initList = np.arange(cityNum)
    # np.random.shuffle(initList)  # 初始解
    # citySolveInit = citySolve(initList)
    initPopulation = createInitPopulation(initList)
    selectPopulation(initPopulation)
    pass
