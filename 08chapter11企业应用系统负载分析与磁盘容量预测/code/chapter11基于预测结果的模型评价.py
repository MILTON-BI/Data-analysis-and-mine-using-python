"""用平均绝对误差、均方根误差和平均绝对百分误差，对模型预测的结果进行评价"""
import pandas as pd
data = pd.read_excel('../outputfiles/模型5天的预测结果.xls')

# 计算误差
abs_ = (data['预测值']/1000000 - data['实际值']/1000000).abs()
mae_ = abs_.mean()   # 平均绝对误差mae
rmse_ = ((mae_ ** 2).mean()) ** 0.5   # 均方根误差rmse
mape_ = (abs_ / (data['实际值']/1000000)).mean()  # 平均绝对百分误差mape

print('平均绝对误差为：%0.6f；\n均方根误差为：%0.6f；\n平均绝对百分误差为：%0.6f。'
    % (mae_, rmse_, mape_))
# 平均绝对误差为：1.055028；
# 均方根误差为：1.055028；
# 平均绝对百分误差为：0.011853。
