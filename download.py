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
        print(r'ffmpeg -i ' + tmp + 'new.ts -acodec copy -vcodec copy -absf aac_adtstoasc ' + root + url[-6:] + '.mp4')
        break
    else :
        i += 1
        

# UPDATE(Apr24,2021)
import os
for vnum in range(451234, 451239) :
    vno = str(vnum)
    i = 0
    url = 'https://xxx/' + vno
    while True :
        try : 
            urlretrieve(url + str(i) + '.ts', tmp + vno + str(i).rjust(4,'0') + '.ts')
        except :
            os.system('copy /b ' + tmp + '*.ts ' + tmp + 'new.ts')
            os.system('ffmpeg -i ' + tmp + 'new.ts -acodec copy -vcodec copy -absf aac_adtstoasc ' + root_test + vno + '.mp4')
            for fi in os.listdir(tmp) :  # del D:\ts\*
                os.remove(tmp + fi)
            break
        else :
            i += 1
