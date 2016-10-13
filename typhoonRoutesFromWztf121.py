# -*- coding:utf-8 -*-
import json
import pandas as pd
import requests


# 生成温州台风网中台风的数据获取地址
def generate_url(code_num):
    base_url = 'http://www.wztf121.com/data/complex/'
    url = base_url + str(code_num) + '.json'
    return url


# 获取指定地址的台风数据
def get_typhoon_data(url):
    '''
    :param url: a url string
    :return: typhoon_data, a dict
            typhoon_data.keys():['points', 'name', 'is_current', 'end_time', 'ename', 'tfbh', 'land', 'begin_time'])
    '''
    headers = {
        'Host': 'www.wztf121.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Referer': 'http://www.wztf121.com/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    typhoon_data = json.loads(res.text)[0]
    return typhoon_data


# 台风路径各点位数据
def get_points(wind_data):
    '''
    :param wind_data: typhoon data, a dict
    :return: points: a list of dict
            points[i].keys():['radius12_quad', 'time', 'speed', 'pressure', 'radius10', 'power', 'strong', 'radius7',
                            'longitude', 'radius7_quad', 'remark', 'radius10_quad', 'forecast', 'move_speed',
                            'latitude', 'radius12', 'move_dir']
    '''
    points = wind_data["points"]
    return points


def one_route(code_num):
    url = generate_url(code_num)
    typhoon_data = get_typhoon_data(url)
    typhoon_name = ''.join([typhoon_data['tfbh'], typhoon_data['ename'], typhoon_data['name']])
    print(typhoon_name)  # 台风名，其形式为'201616Malakas马勒卡'

    routes = get_points(typhoon_data)
    info_keys = ['time', 'longitude', 'latitude', 'pressure', 'strong', 'speed', 'power', 'move_speed', 'move_dir',
                 'radius7', 'radius10', 'radius12']  # 导出数据的列名
    db = pd.DataFrame(routes, columns=info_keys)
    # print(db)
    db.to_csv(typhoon_name + '.csv', index=False)  # 导出csv格式数据


def many_routes(series_nums):
    year, nums = series_nums.split(',')
    start_num, end_num = nums.split('-')
    start_num = int(start_num)
    end_num = int(end_num)
    for i in range(start_num, end_num + 1):
        if 0 < i < 10:
            code_num = year + '0' + str(i)
        elif i >= 10:
            code_num = year + str(i)
        else:
            print('start num error')
            break
        one_route(code_num)


if __name__ == '__main__':

    # 获取单个台风路径数据
    # typhoon_num = input("输入台风代号（如:201605）：")
    # one_route(code_num=typhoon_num)

    # 获取系列台风数据
    typhoon_series_num = input("输入系列台风代号（格式为:2016,05-12）：")
    many_routes(series_nums=typhoon_series_num)
