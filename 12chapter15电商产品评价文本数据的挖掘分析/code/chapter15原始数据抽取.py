import pandas as pd

data = pd.read_csv('../../data2/C15_huizong.csv', encoding='utf-8')
# print(data)   # [215032 rows x 9 columns]
data = data[['评论']][data['品牌'] == '美的']
# print(data)   # [55774 rows x 1 columns]
data.to_csv('../outputfiles/meidi_jd.txt', index=False, header=False)