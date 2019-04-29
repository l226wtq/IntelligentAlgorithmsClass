#!/usr/bin/env python
# encoding: utf-8
'''
@author: 85770
@contact: 14290385@outlook.com
@file: Tabu.py
@time: 2019/3/11 14:21
'''
import copy
import random
import matplotlib.pyplot as plt
import numpy as np
import time

print('hi')
startTime = time.time()
city_x = [41, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 91, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41,
          44, 4]
city_y = [94, 84, 67, 62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 38, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26,
          35, 50]
# 坐标随机生成
# city_randomX = city_x
# city_randomY = city_y
city_randomX = []
city_randomY = []
# cityNum = int(input('enter the num of city:'))
cityNum = 30
swapNum = 14
betterSoFar = 80
Current_tabu = 0
Tabu_linitStep = 10
Tabu_limitLength = 3000


class city:

    def __init__(self, x_l, y_l):
        self.x_localtion = x_l
        self.y_localtion = y_l


class solution():
    def __init__(self, tempList):
        self.solveList = tempList
        self.step = 1
        self.distance = self.calDistance(tempList)

    def calDistance(self, tempList):
        self.tempDistance = 0
        for i, j in zip(tempList, range(cityNum)):
            x = eval('city{}.x_localtion'.format(i))
            y = eval('city{}.y_localtion'.format(i))
            if j == 0:
                x0 = copy.deepcopy(x)
                y0 = copy.deepcopy(y)
            else:
                x2 = eval('city{}.x_localtion'.format(tempList[j - 1]))
                y2 = eval('city{}.y_localtion'.format(tempList[j - 1]))
                self.tempDistance += ((x - x2) ** 2 + (y - y2) ** 2) ** (1 / 2)
                if (j == cityNum - 1):
                    self.tempDistance += ((x - x0) ** 2 + (y - y0) ** 2) ** (1 / 2)
        # print(self.tempDistance) # debug
        return self.tempDistance

    def drawPlot(self):
        plt.clf()
        for i in range(cityNum):
            x = eval('city{}.x_localtion'.format(self.solveList[i]))
            y = eval('city{}.y_localtion'.format(self.solveList[i]))
            plt.scatter(x, y, c='b')
            if i == 0:
                x0 = copy.deepcopy(x)
                y0 = copy.deepcopy(y)
            else:
                x2 = eval('city{}.x_localtion'.format(self.solveList[i - 1]))
                y2 = eval('city{}.y_localtion'.format(self.solveList[i - 1]))
                plt.plot([x, x2], [y, y2], c='r')
                if i == cityNum - 1:
                    plt.plot([x, x0], [y, y0], c='r')  # 忽略编译器错误
        plt.title("distance:%s" % (self.calDistance(self.solveList)))
        plt.pause(0.001)

    def drawPlotOutput(self):
        plt.clf()
        for i in range(cityNum):
            x = eval('city{}.x_localtion'.format(self.solveList[i]))
            y = eval('city{}.y_localtion'.format(self.solveList[i]))
            plt.scatter(x, y, c='b')
            if i == 0:
                x0 = copy.deepcopy(x)
                y0 = copy.deepcopy(y)
            else:
                x2 = eval('city{}.x_localtion'.format(self.solveList[i - 1]))
                y2 = eval('city{}.y_localtion'.format(self.solveList[i - 1]))
                plt.plot([x, x2], [y, y2], c='r')
                if i == cityNum - 1:
                    plt.plot([x, x0], [y, y0], c='r')  # 忽略编译器错误
        plt.title("distance:%s" % (self.calDistance(self.solveList)))
        plt.show()


# 生成随机坐标
# for i in range(cityNum):
#     city_randomX.append(random.randint(0, 200))
#     city_randomY.append(random.randint(0, 200))
for x, y, i in zip(city_x, city_y, range(cityNum)):
    exec('city{}=city(x, y)'.format(i))
    # exec('print(city{}.x_localtion , city{}.y_localtion)'.format(i, i))

init_list = np.arange(cityNum)
Tabu_limitList = np.zeros([cityNum, cityNum])
np.random.shuffle(init_list)
Solution = solution(init_list)
Solution.drawPlot()
# print(Solution.solveList, '\n', Solution.distance)

for i in range(Tabu_limitLength):
    for j in range(cityNum):  # 禁忌计数减一
        for k in range(cityNum):
            if Tabu_limitList[j, k] != 0:
                Tabu_limitList[j, k] = Tabu_limitList[j, k] - 1
    randomList = []
    while len(randomList) < (swapNum * 2):
        x = random.randint(0, cityNum - 1)  # 不能生成等于cityNum的数，会越界
        if x not in randomList:
            randomList.append(x)
    # print('randomList:', randomList)

    # exchange 调换的是排列
    exI = 0
    swapDisList = []
    swapListTemp = []
    swapList = []
    while exI < len(randomList):
        # Solution.solveList[randomList[exI]], Solution.solveList[randomList[exI + 1]] = Solution.solveList[
        #                                                                                    randomList[exI + 1]], \
        #                                                                                Solution.solveList[randomList[exI]]
        # Solution.distance = Solution.calDistance(Solution.solveList)
        swapList = copy.deepcopy(Solution.solveList)
        swapList[randomList[exI]], swapList[randomList[exI + 1]] = swapList[randomList[exI + 1]], swapList[
            randomList[exI]]
        swapListTemp.append(swapList)
        swapDisList.append(Solution.distance - Solution.calDistance(swapList))  # 差值越大越好
        # print('exchange:', swapList, 'Distance:', swapDisList, swapListTemp)
        exI += 2

    swapMax = max(swapDisList)
    if swapMax < 0:
        continue
    maxIndex = swapDisList.index(swapMax)
    # print(swapDisList.index(swapMax))
    if Tabu_limitList[randomList[maxIndex * 2]][randomList[maxIndex * 2 + 1]] == 0:
        Solution.solveList = swapListTemp[maxIndex]
        Solution.distance = Solution.calDistance(Solution.solveList)
        Tabu_limitList[randomList[maxIndex * 2]][randomList[maxIndex * 2 + 1]] = Tabu_linitStep
        Tabu_limitList[randomList[maxIndex * 2 + 1]][randomList[maxIndex * 2]] = Tabu_linitStep  # 禁忌置数
        # Solution.drawPlot()

        # print(Tabu_limitList)
    else:
        if swapMax > betterSoFar:
            Solution.solveList = swapListTemp[maxIndex]
            Solution.distance = Solution.calDistance(Solution.solveList)
            Tabu_limitList[randomList[maxIndex * 2]][randomList[maxIndex * 2 + 1]] = Tabu_linitStep
            Tabu_limitList[randomList[maxIndex * 2 + 1]][randomList[maxIndex * 2]] = Tabu_linitStep  # 禁忌置数
            Solution.drawPlot()
            # print(Tabu_limitList)
        else:
            # print('In Tabu,banned!')
            continue
endTime = time.time()
print('time', endTime - startTime)
Solution.drawPlotOutput()
# for i in range(10):
#     np.random.shuffle(init_list)  # 随机排列
#     print(init_list)

# city1 = city(10, 32)
# city2 = city(235, 12)
# distance1 = Distance(city1.x_localtion, city1.y_localtion, city2.x_localtion, city2.y_localtion)
# print(distance1.distance)
