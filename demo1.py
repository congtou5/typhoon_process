# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math

filename = 'F:\\PythonWorkplace\\TyphoonDataProcess\\typhoonData\\201212Haikui.csv'
station = [122.25, 31.14]


def get_max_radius(typhoon, k):
    # 梅花最大风速半径
    if typhoon == 'Muifa':
        rmax = 140000

    # 灿鸿最大风速半径
    if typhoon == 'Chanhom':
        if k < 16:
            rmax = 90000
        elif k < 19:
            rmax = 50000
        elif k == 19:
            rmax = 15000
        elif k == 20:
            rmax = 10000
        elif k == 21:
            rmax = 60000
        else:
            rmax = 120000

    # 海葵最大风速半径
    if typhoon == 'Haikui':
        if k > 29:
            rmax = 280000
        elif k == 29:
            rmax = 200000
        elif k == 28:
            rmax = 175000
        elif k == 27:
            rmax = 70000
        elif k == 26:
            rmax = 50000
        else:
            rmax = 40000

    # 麦德姆最大风速半径
    if typhoon == 'Matmo':
        if k < 26:
            rmax = 80000
        elif k == 33:
            rmax = 200000
        elif k == 34:
            rmax = 260000
        else:
            rmax = 180000

    # 天秤最大风速半径
    if typhoon == 'Tembin':
        if k >= 20 and k <= 25:
            rmax = 180000
        elif k >= 32:
            rmax = 40000
        else:
            rmax = 140000

    # 布拉万最大风速半径
    if typhoon == 'Bolaven':
        if k >= 35:
            rmax = 175000
        else:
            rmax = 80000

    return rmax


def get_angle(x, y):
    s = math.sqrt(x ** 2 + y ** 2)
    if x > 0:
        angle = 270 - math.asin(y / s) * 180 / math.pi
    else:
        angle = 90 + math.asin(y / s) * 180 / math.pi
    return angle


def typhoon_simulation(filename, staion):
    data = pd.read_csv(filename)
    data = data.loc[:, 'time':'airpre']
    row, col = data.shape

    typhoon = 'Haikui'
    lat_distance = 111000  # 1纬度的距离
    time_interval = 6 * 3600  # 每个路径点的时间间隔
    vdxs = []
    vdys = []  # 台风移动速度
    rmaxs = []
    lon_distances = []
    dxs = []
    dys = []
    ds = []  # 点到每个台风中心距离
    vmxs = []
    vmys = []  # 移行风场数据
    wxs = []
    wys = []
    angles = []
    for i in range(row):
        typhoon_center = data.loc[i, :]

        # 求科氏力参数
        # f=coriolis_parameter
        f = 2 * 2 * math.pi / (24 * 3600) * math.sin(typhoon_center['lat'] * math.pi / 180)

        lon_distance = lat_distance * math.cos(data.loc[i, 'lat'] * math.pi / 180)  # 1经度的距离
        lon_distances.append(lon_distance)
        # 计算台风移动速度
        if i != row - 1:
            vdx = (data.loc[i + 1, 'lon'] - data.loc[i, 'lon']) * lon_distance / time_interval
            vdy = (data.loc[i + 1, 'lat'] - data.loc[i, 'lat']) * lat_distance / time_interval
            vdxs.append(vdx)
            vdys.append(vdy)
        else:
            vdx = (data.loc[i, 'lon'] - data.loc[i - 1, 'lon']) * lon_distance / time_interval
            vdy = (data.loc[i, 'lat'] - data.loc[i - 1, 'lat']) * lat_distance / time_interval
            vdx = vdx * 0.8
            vdy = vdy * 0.8
            vdxs.append(vdx)
            vdys.append(vdy)

        # 计算点与i时刻台风中心的坐标差及距离
        dx = (station[0] - typhoon_center['lon']) * lon_distances[i]
        dy = (station[1] - typhoon_center['lat']) * lat_distance
        s = math.sqrt(dx ** 2 + dy ** 2)
        dxs.append(dx)
        dys.append(dy)
        ds.append(s)

        # 计算最大风速半径
#        vd = math.sqrt(vdx ** 2 + vdy ** 2)
#        rmax = 28.52 * math.tanh(0.0873 * (typhoon_center['lat'] - 28) * math.pi / 180) + \
#               12.22 * math.exp((typhoon_center['airpre'] / 100 - 1013.3) / 33.86) + 0.2 * vd + 37.22
#        rmax = rmax * 1000
        rmax = get_max_radius(typhoon, i)
        rmaxs.append(rmax)

        # k时刻气压差
        dp = 1013.3 * 100 - typhoon_center['airpre']

        # 移行风场
        vmx = vdx * math.exp(-math.pi / 4 * abs(s - rmax) / rmax)
        vmy = vdy * math.exp(-math.pi / 4 * abs(s - rmax) / rmax)
        vmxs.append(vmx)
        vmys.append(vmy)

        # 梯度风场
        if s <= 2 * rmax:
            temp = 2 * dp / (1.29 * (rmax ** 2)) * math.pow(1 + 2 * ((s / rmax) ** 2), -3 / 2)
            vg = -f / 2 + math.sqrt((f ** 2) / 4 + temp)
        else:
            temp = dp / (1.29 * ((1 + s / rmax) ** 2) * rmax * s)
            vg = -f / 2 + math.sqrt(f ** 2 / 4 + temp)

        # 计算的模拟风场
        coef1 = 1.0
        coef2 = 0.8
        wx = coef1 * vg * (-dx * math.sin(math.pi / 9) - dy * math.cos(math.pi / 9)) + coef2 * vmx
        wy = coef1 * vg * (dx * math.cos(math.pi / 9) - dy * math.sin(math.pi / 9)) + coef2 * vmy
        angle = get_angle(wx, wy)
        angles.append(angle)
        wxs.append(wx)
        wys.append(wy)
    return rmaxs, wxs, wys, angles


rmaxs, wxs, wys, angles = typhoon_simulation(filename, station)
arr1 = np.array(wxs)
arr2 = np.array(wys)
w = np.sqrt(arr1 ** 2 + arr2 ** 2)
