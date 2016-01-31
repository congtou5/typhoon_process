# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from math import *
import os


def xy_to_ll(x, y):
    npjx = 428630.0
    npjy = 3446000.0
    ncdx = 414095.8600
    ncdy = 3431351.7690
    lon = 122.11 + (x - ncdx) * (122.25 - 122.11) / (npjx - ncdx)
    lat = 31.02 + (y - ncdy) * (31.14 - 31.02) / (npjy - ncdy)
    return lon, lat


def calculate_typhoon(datetime, route, xy, ff):
    coef1 = 1.0
    coef2 = 0.8
    f1 = open(ff+'\\wind.swan', 'w')

    for k in range(route.shape[0]):
        lon, lat = xy_to_ll(route[k, 0], route[k, 1])

		# 科氏力参数
        f = 2 * 2 * pi / (24 * 3600) * np.sin(lat * pi / 180)
        # print f

		# 台风移动速度
        vdx = 0
        vdy = route[k, 4] / 3.6

		# 牛皮礁与台风中心的距离
        dx = xy[:, 0] - route[k, 0]
        dy = xy[:, 1] - route[k, 1]
        s = np.sqrt(dx ** 2 + dy ** 2)
        #    print s.shape

		# 气压差
        dp = (1013.3 - route[k, 2]) * 100

		# 最大风速半径
        r_max = route[k, 3] * 1000

        vmx = vdx * np.exp(-pi / 4 * abs(s - r_max) / r_max)
        vmy = vdy * np.exp(-pi / 4 * abs(s - r_max) / r_max)

        # 梯度风场
        vg = []
        for i in range(s.shape[0]):
            if s[i] <= 2 * r_max:
                temp = 2 * dp / (1.29 * (r_max ** 2)) * np.power(1 + 2 * ((s[i] / r_max) ** 2), -3 / 2)
                vg.append(-f / 2 + np.sqrt((f ** 2) / 4 + temp))
            else:
                temp = dp / (1.29 * ((1 + s[i] / r_max) ** 2) * r_max * s[i])
                vg.append(-f / 2 + np.sqrt(f ** 2 / 4 + temp))
        vg = np.array(vg)

        # 模拟风场
        wx = coef1 * vg * (-dx * sin(pi / 9) - dy * cos(pi / 9)) + coef2 * vmx
        wy = coef1 * vg * (dx * cos(pi / 9) - dy * sin(pi / 9)) + coef2 * vmy
        w = np.concatenate((wx, wy), axis=0)

        out_file = ''.join(datetime[k, 0].split('/')) + '.' + ''.join(datetime[k, 1].split(':')) + '.wind'
        f1.write(out_file + '\n')
        out_file = ff + '\\' + out_file
        np.savetxt(out_file, w, fmt='%.3f')
    f1.close()


fort_name = 'F:\\jiaxiao\\OrthogonalExperimentalDesign(matlab)\\fort.txt'
xy = np.loadtxt(fort_name)
path_files = os.listdir('F:\\jiaxiao\\OrthogonalExperimentalDesign(matlab)')
for ff in path_files:
    fname = ff + '\\swan.txt'
    if not os.path.exists(fname):
        continue
    data = pd.read_table(fname, sep=' ', header=None,
                        names=['date', 'time', 'x', 'y', 'pre', 'rad', 'vel'])
    route = np.array(data.loc[:, 'x':'vel'])
    datetime = np.array(data.loc[:, 'date':'time'])
    calculate_typhoon(datetime, route, xy, ff)
