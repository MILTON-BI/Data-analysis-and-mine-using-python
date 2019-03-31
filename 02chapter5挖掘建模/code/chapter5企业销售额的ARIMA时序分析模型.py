import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 参数初始化
inputfile = '../../data1/arima_data.xls'
forecastnum = 5
# 读取数据，指定日期列为index，pandas会自动将日期列识别为datetime格式
data = pd.read_excel(inputfile, index_col=u'日期')
# print(data1)

# 绘制时序图
data.plot()
# plt.show()
# plt.savefig('../outputfiles/arima时序分析时序图.png')

# 绘制自相关图
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data)
# plt.show()
# plt.savefig('../outputfiles/arima时序分析自相关图.jpg')

# 平稳性检测
from statsmodels.tsa.stattools import adfuller as ADF
print(u'原始序列的ADF检验结果为：', ADF(data[u'销量']))
# (1.8137710150945274, 0.9983759421514264, 10, 26, {'1%': -3.7112123008648155, '5%': -2.981246804733728, '10%': -2.6300945562130176}, 299.46989866024177)
# 返回值依次为：adf, pvalue, usedlag, nobs, critical values, icbest, regresults, resstore

# 差分并显示结果
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
D_data.plot()   # 时序图
# plt.show()
# plt.savefig('../outputfiles/arima时序分析差分后的时序图')
plot_acf(D_data)  # 自相关图
# plt.show()
# plt.savefig('../outputfiles/arima时序分析差分后的自相关图.jpg')

# 绘制差分后的偏自相关图
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(D_data)   # 偏自相关图
# plt.show()
# plt.savefig('../outputfiles/arima时序分析差分后的偏自相关图.png')
print(u'差分序列的ADF检验结果为：', ADF(D_data[u'销量差分']))   # 输出平稳性检测的结果

# 白噪声检测
from statsmodels.stats.diagnostic import acorr_ljungbox
print(u'差分序列的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))  # 显示白噪声检测结果(统计量和p值)

# arima模型分析
from statsmodels.tsa.arima_model import ARIMA
# 定阶
pmax, qmax = int(len(D_data) / 10), int(len(D_data) / 10)  # 一般阶数不超过length/10
bic_matrix = []   # bic矩阵初始化
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try: # 存在部分报错，所以用try来跳过报错
            tmp.append(ARIMA(data, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)


bic_matrix = pd.DataFrame(bic_matrix)   # 从中可以找出最小值
p, q = bic_matrix.stack().idxmin()    # 先用stack展平，然后用idxmin找出最小值位置
print(u'BIC最小的p值和q值为：%s、 %s' % (p, q))
model = ARIMA(data, (p, 1, q)).fit()    # 建立Arima(0,1,1)模型并训练
print(model.summary2())    # 给出一份模型报告
print(model.forecast(5))   # 做为期5天的预测，返回预测结果、标准误差、置信区间
