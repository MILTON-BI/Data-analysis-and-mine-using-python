import pandas as pd

data = pd.read_excel('../../data2/C11_discdata.xls')
# print(data)

data = data[data['TARGET_ID'] == 184].copy() # 只保留target_id为184的数据

data_group = data.groupby('COLLECTTIME')  # 按时间分组
# print(dict(list(data['ENTITY'].groupby(data['COLLECTTIME']))))

# 定义属性变换函数
def attr_trans(x):
    result = pd.Series(index=['SYS_NAME',
                              'CWXT_DB:184:C\\',
                              'CWXT_DB:184:D\\',
                              'COLLECTTIME'])
    result['SYS_NAME'] = x['SYS_NAME'].iloc[0]
    result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]
    result['CWXT_DB:184:C\\'] = x['VALUE'].iloc[0]
    result['CWXT_DB:184:D\\'] = x['VALUE'].iloc[1]
    return result
data_processed = data_group.apply(attr_trans)  # 逐组处理
data_processed.to_excel('../outputfiles/data_processed.xls', index=False)
