# -*- coding: utf-8 -*-
import numpy as np
from math import *


class centerPoint():
    def __init__(self, route, num, point):
        self.num = num
        self.center = route[num]
        # self.longitude = self.center['lon']
        # self.latitude = self.center['lat']
        # self.pressure = self.center['pre']
        self.point_lon = point['lon']
        self.point_lat = point['lat']
        self.lat_dis = 111000
        self.lon_dis = self.lat_dis * sin(self.center[1] * pi / 180)
        self.dt = 6 * 3600
        self.f = self.coriolis_parameter()

    def coriolis_parameter(self):
        f = 2 * 2 * pi / (24 * 3600) * sin(self.point_lat * pi / 180)
        return f

    def moving_speed(self, vd=None):
        if vd is not None:
            return vd['x'], vd['y']
        k = self.num
        vdx = (self.center[k + 1, 0] - self.center[k, 0]) * self.lon_dis / self.dt
        vdy = (self.center[k + 1, 1] - self.center[k, 1]) * self.lat_dis / self.dt
        return vdx,vdy
