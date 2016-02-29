# -*- coding:utf-8 -*-
from math import *


class sedimentationIntensity:
    def __init__(self):
        '''
        b 航道宽度
        g 重力加速度（m/s²）
        gamma 水的容重（kg/m³）
        gamma_s 泥沙容重（kg/m³）
        T 波浪周期（s）
        d 水深（m）
        L 波长（m）
        H_deci 十分之一波高（m）
        '''
        self.b = 1
        self.g = 9.8
        self.gamma = 1000
        self.gamma_s = 2650
        self.T = 1
        self.d = 1
        self.L = 1
        self.H_deci = 1

    # def settling_rate(self):

    # 干容重计算
    @staticmethod
    def dry_density(D50):
        '''
        D50 淤积物颗粒的中值粒径 单位:mm
        gamma 单位:kg/m³
        '''
        gamma = 1750 * (D50 ** 0.183)
        return gamma

    def wave_max_water_vel(self, wave_break):
        '''
        wave_break 值为1或0
        u_w 波浪最大水质点速度（m/s）
        Hb 破波波高（m）
        d_b 破碎水深（m）
        gamma_b 破波指标
        '''
        Hb = 1
        d_b = 1
        gamma_b = Hb / d_b
        if wave_break:
            u_w = 0.5 * sqrt(self.g * gamma_b * Hb)
        else:
            u_w = pi * self.H_deci / (self.T * sinh(2 * pi * self.d / self.L))
        return u_w

    def vertical_average_sediment_content(self):
        '''
        S1 垂线平均含沙量
        :return:
        '''
        alpha = 0.075 * (10 ** -3)
        beta = 0.64
        u_c = 1
        u_w = self.wave_max_water_vel(1)
        d_1 = 1
        omega = 1
        temp1 = self.gamma_s * self.gamma / (self.gamma_s - self.gamma)
        temp2 = (u_c + beta * u_w) ** 3 / (self.g * d_1 * omega)
        S1 = alpha * temp1 * temp2
        return S1

    def bottom_high_sediment_water_height(self, D50):
        '''
        sigma 波浪圆频率
        omega_d 底部泥沙颗粒沉降速度（m/s）
        k 波数
        '''
        k = 1
        sigma = 2 * pi / self.T
        eta = 200 * D50
        omega_d = 1
        a_m = self.H_deci / (2 * sinh(k * self.d))
        h_s = 0.1 * a_m * sigma / omega_d * eta
        return h_s

    # 底部高浓度含沙水体平均含沙量
    def bottom_average_sediment_content(self):
        n = 0.2
        R = 1
        C = 1 / n * (R ** (1 / 6))
        C0 = C / sqrt(self.g)
        _u = 1
        f_w = 0.015
        u_w = self.wave_max_water_vel(0)
        uxc = _u / C0
        uxw = sqrt(f_w / 2) * u_w
        Ux = sqrt(uxw ** 2 + uxc ** 2)
        S1 = self.vertical_average_sediment_content()
        h_s = self.bottom_high_sediment_water_height(D50=1)
        coef1 = -omega_d / (0.12 * 0.4 * Ux)
        coef2 = (omega_d - omega_s) * (0.35 * self.d - 0.5 * h_s) / (0.12 * 0.4 * Ux * self.d)
        _Sd = S1 * pow((0.5 * h_s / 0.35 * (self.d)), coef1) * exp(-coef2)
        return _Sd

    # 底部平均流速
    def bottom_average_vel(self):
        K = 0.4

        h_s = self.bottom_high_sediment_water_height(D50=1)
        if Ux * k_s / nu < 5:
            Bs = 2.5 * log(Ux * k_s / nu) + 5.5
        elif Ux * k_s / nu >= 70:
            Bs = 8.5
        if h_s >= 0.15:
            u_d = (1 / K * log(0.5 * h_s / k_s) + Bs) * uxc
        return u_d

    # 悬疑质淤积强度
    def suspended_sediment_intensity(self):
        alpha = 0.60
        omega = 1
        Ss = self.vertical_average_sediment_content()
        t1 = 1
        gamma_0 = 1
        d1 = 1
        d2 = 1
        theta = 1
        temp1 = alpha * omega * Ss * t1 / gamma_0
        temp2 = 1 - (d1 / d2) ** 0.56 * (cos(theta * pi / 180) ** 2) - (d1 / d2) ** 3 * (sin(omega * pi / 180) ** 2)
        Ps = temp1 * temp2
        return Ps

    # 底部高浓度含沙水体输移淤积强度
    def bottom_sediment_intensity(self):
        u_d = self.bottom_average_vel()
        h_s = self.bottom_high_sediment_water_height(D50=1)
        _Sd = self.bottom_average_sediment_content()
        t2 = 1
        gamma_01 = 1
        b = 1
        theta = 1
        if h_s <= 0.1:
            Pd = 0
        else:
            Pd = u_d * h_s * _Sd * t2 / (gamma_01 * b) * sin(theta * pi / 180)
        return Pd

    # 推移质淤积强度
    def bed_load_intensity(self):
        alpha_b = 0.01
        gamma_02 = 1
        omega_b = 1
        D50 = 1
        u_e = 1
        t3 = 1
        theta = 1
        u_c = 1
        Hs = 1
        T = 1
        d = 1
        L = 1
        u_w = pi * Hs / (T * sinh(2 * pi * d / L))
        u_cw = sqrt(u_c ** 2 + u_w ** 2)
        temp1 = self.gamma_s * self.gamma / ((self.gamma_s - self.gamma) * gamma_02)
        temp2 = (1 - (u_e / u_cw) ** 2) * (u_cw ** 3) * t3 / (self.g * self.b) * sin(theta)
        Pb = alpha_b * temp1 * omega_b / sqrt(self.g * D50) * temp2

        return Pb

    # 淤积强度
    @staticmethod
    def total_intensity(Ps, Pd, Pb):
        P = Ps + Pd + Pb
        return P


if __name__ == '__main__':
    s = sedimentationIntensity()
    Ps = s.suspended_sediment_intensity()
    Pd = s.bottom_sediment_intensity()
    Pb = s.bed_load_intensity()
    P = s.total_intensity(Ps, Pd, Pb)
