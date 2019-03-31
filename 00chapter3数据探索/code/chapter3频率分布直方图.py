import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('../data1/catering_sale.xls')
jicha = data['销量'].max() - data['销量'].min()
print(jicha)  # 9084.44
zuju = round(jicha / 500)
print(zuju)   # 18

sale_data = data['销量']
n, bins, patches = plt.hist(sale_data, bins=9)
plt.show()
print(n, bins, patches)
# [  4.   2. 150.  40.   2.   0.   1.   0.   1.] [  22.   1031.38222222 2040.76444444 3050.14666667 4059.52888889  5068.91111111 6078.29333333 7087.67555556 8097.05777778 9106.44 ]