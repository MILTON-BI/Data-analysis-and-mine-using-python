import pandas as pd

threshold = pd.Timedelta(minutes=4)
# print(threshold)    # 0 days 00:04:00

data = pd.read_excel('../../data2/C10_water_heater.xls')
# print(data[:10])  # 以下为输出数据
#       发生时间 开关机状态 加热中 保温中  实际温度 热水量  水流量 加热剩余时间 当前设置温度
# 0  20141019063917     关   关   关  30°C  0%    0    0分钟   50°C
# 1  20141019070154     关   关   关  30°C  0%    0    0分钟   50°C
# 2  20141019070156     关   关   关  30°C  0%    8    0分钟   50°C
# 3  20141019071230     关   关   关  30°C  0%    0    0分钟   50°C
# 4  20141019071236     关   关   关  29°C  0%    0    0分钟   50°C

data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')
# print(data['发生时间'][:5])   # 以下为输出数据
# 0   2014-10-19 06:39:17
# 1   2014-10-19 07:01:54
# 2   2014-10-19 07:01:56
# 3   2014-10-19 07:12:30
# 4   2014-10-19 07:12:36

# 只选取流量大于0的记录
data = data[data['水流量'] > 0]
# 对相邻时间做差分，比较是否大于阈值
d = data['发生时间'].diff() > threshold
# print(d)    # 以下是输出
# 2        False
# 56        True
# 381       True
# 382      False
# 384      False

# 通过累积求和的方式为事件编号
data['事件编号'] = d.cumsum() + 1

# 保存处理后的文件
# data.to_excel('../outputfiles/划分完整用水事件.xls')