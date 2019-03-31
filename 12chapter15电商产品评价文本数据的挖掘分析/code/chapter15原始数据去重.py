import pandas as pd

data = pd.read_csv('../outputfiles/meidi_jd.txt', encoding='utf-8', header=None)
# print(data)  #  [55774 rows x 1 columns]
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
# print(l1, l2)   #  55774 53049
data.to_csv('../outputfiles/meidi_jd_1_quchong.txt', index=False, header=False, encoding='utf-8')
print('共删除了%s条评论' % (l1-l2))