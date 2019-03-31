import pandas as pd
import numpy as np

data = pd.read_excel('../../data2/C10_water_heater.xls')
n = 4   # 使用以后4个点的平均斜率
threshold = pd.Timedelta(minutes=5)   # 专家阈值
data = data[data['水流量'] > 0 ]    # 只取水流量大于0的记录
data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')

def event_num(ts):
    d = data['发生时间'].diff() > ts   # 相邻时间做差分，比较是否大于阈值
    return d.sum() + 1   # 直接返回事件数

dt = [pd.Timedelta(minutes = i) for i in np.arange(1, 9, 0.25)]
# print(dt)  # 以下是输出结果
# [Timedelta('0 days 00:01:00'), Timedelta('0 days 00:01:15'), Timedelta('0 days 00:01:30')...]


h = pd.DataFrame(dt, columns=['阈值'])  # 定义阈值列
# print(h)   # 以下是输出结果
#        阈值
# 0  00:01:00
# 1  00:01:15
# 2  00:01:30
# 3  00:01:45

h['事件数'] = h['阈值'].apply(event_num)   # 计算每个阈值对应的事件数
h['斜率'] = h['事件数'].diff() / 0.25    # 计算每两个相邻点对应的斜率
h['斜率指标'] = h['斜率'].abs().rolling(n).mean()  # 采用后n个的斜率绝对值平均作为斜率指标
ts = h['阈值'][h['斜率指标'].idxmin() - n]
# 用idxmin返回最小的index，由于rolling.mean()自动计算的是前n个斜率的绝对值平均，所以结果要平移-n

if ts > threshold:
    ts = pd.Timedelta(minutes=4)
print(ts)   # 0 days 00:04:00, 该结果表示最优阈值为4分钟



