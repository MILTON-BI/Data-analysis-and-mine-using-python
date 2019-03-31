
import pandas as pd
lagnum = 12   # 指定残差延迟个数

data = pd.read_excel('../outputfiles/data_processed.xls', index_col='COLLECTTIME')
data = data.iloc[: len(data)-5]   # 不使用最后5个数据
x_data = data['CWXT_DB:184:D\\']

from statsmodels.tsa.arima_model import ARIMA
# 建立ARIMA(1,1,1)模型
arima = ARIMA(x_data, (1, 1, 1)).fit()   # 建立并训练模型
x_data_predict = arima.predict(typ='levels')   # 预测
pred_error = (x_data_predict - x_data).dropna()  # 计算残差

from statsmodels.stats.diagnostic import acorr_ljungbox  # 白噪声检测
lb, p = acorr_ljungbox(pred_error, lags=lagnum)
h = (p < 0.05).sum()  # p小于0.05,认为是非白噪声
if h > 0:
    print('模型ARIMA(1,1,1)不符合白噪声检验')
else:
    print('模型ARIMA(1,1,1)符合白噪声检验')
# 如果不是白噪声，说明残差中还存在有用信息，需要修改模型或进一步提取
# 本代码的ARIMA(1,1,1)模型符合白噪声检验

# 训练模型并进行预测（5天），并输出结果
print(arima.summary2())    # 给出一份模型报告
pred_result, pred_std, pred_confidence_interval = arima.forecast(5)
# 做为期5天的预测，返回预测结果、标准误差、置信区间
# print(pred_result)
# print(pred_std)
# print(pred_confidence_interval)
data_for_pred = pd.read_excel('../outputfiles/data_processed.xls', index_col='COLLECTTIME')
data_for_pred = data_for_pred.iloc[-5:]
predict_data = pd.DataFrame({'预测值': list(pred_result),
                             '标准误差': list(pred_std),
                             '置信区间': list(pred_confidence_interval),
                             '实际值': data_for_pred['CWXT_DB:184:D\\']},
                            index=data_for_pred.index)
# print(predict_data)
predict_data.to_excel('../outputfiles/模型5天的预测结果.xls')   # 结果输出到文件