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
