def ftext(n) :
    ''' Merge MP4 files '''
    s = ''
    for i in range(n) :
        print('ffmpeg -i \'' + 'video '
              + '(' + str(i+1) +').mp4\' -vcodec copy -acodec copy -vbsf h264_mp4toannexb ' + str(i+1) + '.ts')
        s = s + str(i+1) + '.ts'
        if i != n-1 :
            s += '|'
    print('ffmpeg -i \'concat:' + s + '\' -acodec copy -vcodec copy -absf aac_adtstoasc output.mp4')

ftext(3)

# .wmv to .mp4
for i in range(3) :
    print('ffmpeg -i \'(' + str(i+1) +').wmv\' \'(' + str(i+1) + ').mp4\'')

# mpeg4 to h264
for i in range(5) :
    print('ffmpeg -i \'(' + str(i+1) +').mp4\' -vcodec h264 \'video (' + str(i+1) + ').mp4\'')
