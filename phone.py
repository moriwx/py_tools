import pandas as pd
import phone

phone.Phone().find(14514191981).keys()

df = pd.read_csv('ph.csv')
for i in ['province', 'city', 'zip_code', 'area_code', 'phone_type']:
    df[i] = df.tel.map(lambda x : phone.Phone().find(x)[i])
df.to_csv('ph1.csv', index=False, encoding='utf_8_sig')
