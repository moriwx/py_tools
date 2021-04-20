from urllib.request import urlretrieve
tmp = r'D:\\ts\\'
root = r'E:\\Videos\\'

taskno = '123'
url = 'https://xxx/123456'

i = 0
while True :
    try :
        urlretrieve(url + str(i) + '.ts', tmp + taskno + str(i).rjust(4,'0') + '.ts')
    except :
        print('copy /b ' + tmp + '*.ts ' + tmp + 'new.ts')
        print(r'ffmpeg -i ' + tmp + 'new.ts -acodec copy -vcodec copy -absf aac_adtstoasc '
              + root + url[-6:] + '.mp4')
        break
    else :
        i += 1
        
# del D:\ts\*
