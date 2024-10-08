
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

# プロセカ曲
import re
import pandas as pd

def link_extract(text):
    match = re.search(r'\[\[(.*?)\]\]', text)
    if match:
        return match.group(1)
    else:
        return text

def maapd_extract(text):
    match_ma = re.search(r'{{color\|#884499\|(\d{1,4})}}', text.replace("'", ''))
    match_apd = re.search(r'{{color\|#FF77DD\|(\d{1,4})}}', text)
    if match_apd:
        return (match_ma.group(1), match_apd.group(1))
    return (match_ma.group(1),)
    
data = []
with open('E://Music//プロセカ曲.txt', 'r', encoding='utf-8') as file: # 20240830
    for line in file:
        if len(line)>=5 and line.startswith('|'):
            datai = line.lstrip('|').rstrip('\n').split('||')
            if len(datai)==17:
                data.append(datai)
            else: print(datai)
columns = ['id', 'date', 'title', 'artist', 'bpm', 'duration', 'ez', 'nr', 'hd', 'ex',
          'maapd', 'ezn', 'nrn', 'hdn', 'exn', 'maapdn', 'info']
df = pd.DataFrame(data, columns=columns)
df.title = df.title.apply(link_extract)
df.artist = df.artist.apply(link_extract)
df.maapd = df.maapd.apply(maapd_extract)
df.maapdn = df.maapdn.apply(maapd_extract)

def apd_date_cal(row):
    if len(row.maapd)==2:
        apddatel = re.findall(r'\d{4}/\d{2}/\d{2}', row['info'])
        if len(apddatel)==1:
            return apddatel[0]
        # elif len(apddatel)>1: print(row)
        else:
            return row['date']
    return ''
df['appdate'] = df.apply(apd_date_cal, axis=1)

def band_genre(text):
    if text.startswith('Leo/need'):
        return 'ln'
    if text.startswith('MORE MORE JUMP!'):
        return 'mmj'
    if text.startswith('Vivid BAD SQUAD'):
        return 'vbs'
    if text.startswith('Wonderlands×Showtime'):
        return 'ws'
    if text.startswith('25点，Nightcord见。'):
        return '25'
    if text.startswith('世界计划虚拟歌手'):
        return 'v'
    if text.startswith('世界计划其他歌曲'): # 待细分
        return 'other'
    return ''
df['band'] = df.title.apply(band_genre)
df['genre'] = df.title.str.extract(r'^(.*?)\d{0,1}#', expand=True)
df.loc[df.id.isin(('76', '77', '141', '235', '336', '366', '489', '502')), 'band'] = 'v'
df.loc[df.id.isin(('302', '232', '233')), 'band'] = 'ln'
df.loc[df.id.isin(('400',)), 'band'] = 'mmj'
df.loc[df.id.isin(('230',)), 'band'] = 'vbs'
df.loc[df.id.isin(('234',)), 'band'] = 'ws'
df.loc[df.id.isin(('231', '501')), 'band'] = '25'

def title_extract(text):
    match = re.search(r'\|(.*?)$', text)
    if match:
        match1 = re.search(r'^{{lj\|(.*?)}}$', match.group(1))
        if match1:
            return match1.group(1)
        return match.group(1)
    return text
df.title = df.title.apply(title_extract)

df.to_excel('pjsk.xls')
