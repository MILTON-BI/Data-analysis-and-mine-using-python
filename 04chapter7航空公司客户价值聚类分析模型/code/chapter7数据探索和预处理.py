"""
航空公司客户价值聚类分析模型代码
1. 数据记录62299
2. 模型：LRFMC
    L：客户关系长度（客户入会时间距观测窗口结束时间的月数）
    R：客户最近一次乘坐本司飞机距观测窗口结束时间的月数
    F：客户在观测窗口内乘坐本司飞机飞行的次数
    M：客户在观测窗口内累计的飞行里程
    C：客户在观测窗口内乘坐仓位所对应的折扣系数的平均值
    通过上面模型的五个指标进行K-means聚类，识别最有价值的客户

"""
import pandas as pd
import numpy as np

"""数据读取，并进行初步的数据探索分析：返回缺失值个数，及最大、最小值"""
datafile = '../../data2/C7_air_data.csv'   # 数据文件
data_outputfile = '../outputfiles/data_explore_result.xls'   # 探索结果输出文件

data = pd.read_csv(datafile, encoding='utf-8')  # 读取数据，指定为utf-8格式
explore = data.describe(percentiles=[], include='all').T
# 包括对数据的基本描述，percentiles参数指定计算多少分位数；T进行转置，方便查阅
"""describe函数自动计算的字段有：
   count(非空值数)、unique(唯一值数)、top(频数最高者)、freq(最高频数)、
   mean(均值)、std(方差)、min(最小值)、50%(中位数)、max(最大值)
"""
# explore.to_excel('../outputfiles/data_explore_describe.xls')  # 保存describe的结果
# print(explore)   # [44 rows x 9 columns]

explore['null'] = len(data) - explore['count']  # describe自动计算非空值数，需要手动计算空值数
explore_result = explore[['null', 'max', 'min']]    # 这里只选取空值、最大值和最小值
explore_result.columns = [u'空值数', u'最大值', u'最小值']   # 重命名表头
# explore_result.to_excel(data_outputfile)


"""数据预处理
   1. 数据清洗：因数据量大，丢弃票价为空的记录，以及票价为0，平均折扣不为0，总飞行公里数大于0的记录
   """

# 票价非空值才保留
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
# print(data[['SUM_YR_1', 'SUM_YR_2']])

# 只保留票价非0，或者平均折扣率和飞总总里程同时为0的记录
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
data = data[index1 | index2 | index3]
# 导出清洗过的数据
# data.to_excel('../outputfiles/data_cleaned.xls')

"""数据预处理
   2. 数据规约：原始数据属性太多，根据航空公司的LRFMC模型，只选择相关的6个属性：
      FFP_DATA, LOAD_TIME, FLIGHT_COUNT, AVG_DISCOUNT, SEG_KM_SUM, LAST_TO_END
      其余不相关属性删除
   """
model_data = data[['FFP_DATE', 'LOAD_TIME', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]
# model_data.to_excel('../outputfiles/删除不相关属性后的数据.xls')
# print(len(model_data))

"""数据预处理
   3. 根据LRFMC模型做数据变换
   （1）属性构造：
        L = LOAD_TIME - FFP_DATE
        R = LAST_TO_END
        F = FLIGHT_COUNT
        M = SEG_KM_SUM
        C = avg_discount
   （2）数据归一化：均值-方差归一化
   """
import datetime
L = []
for i in range(len(model_data)):
    t1_year = datetime.datetime.strptime(model_data['LOAD_TIME'].iloc[i], '%Y/%m/%d').year
    t1_month = datetime.datetime.strptime(model_data['LOAD_TIME'].iloc[i], '%Y/%m/%d').month + 1
    t2_year = datetime.datetime.strptime(model_data['FFP_DATE'].iloc[i], '%Y/%m/%d').year
    t2_month = datetime.datetime.strptime(model_data['FFP_DATE'].iloc[i], '%Y/%m/%d').month
    t2_day = datetime.datetime.strptime(model_data['FFP_DATE'].iloc[i], '%Y/%m/%d').day
    if t2_day >= 15:
        duration_months = (t1_year - t2_year) * 12 + (t1_month - (t2_month + 1))
    else:
        duration_months = (t1_year - t2_year) * 12 + (t1_month - t2_month)
    L.append(duration_months)
# print(len(L))
model_data = pd.concat([pd.DataFrame(L, index=model_data.index), model_data[['LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]], axis=1)
# print(model_data)
model_data.columns = ['L', 'R', 'F', 'M', 'C']
# print(model_data)
# 对数据进行均值-标准差归一化处理
model_data_norm = (model_data - model_data.mean(axis=0)) / model_data.std(axis=0)
# print(model_data_norm)
model_data_norm.to_excel('../outputfiles/经过清洗和预处理的数据.xls', index=False)

