
# 19OCT22
import pandas as pd
path = ''
df1 = pd.read_excel(path+'流调表.xlsx',engine='openpyxl')
df2 = pd.read_excel(path+'身份证号.xlsx',engine='openpyxl')
df3 = pd.merge(df1,df2, how='outer')
df3[df3.分班==10].to_excel(path+'new.xls')

# 23MAR23
stockdata = pd.read_csv('./1.csv')
money=[0]
def mmm(x):
    if x['signal'] == 1: money[0] += x['equity_change']
    else: money[0] -= 1
    return
stockdata.apply(mmm, axis=1)
