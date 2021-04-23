import os
from urllib.request import urlretrieve
root = r'E:\\MCM21\\'
mcm = 'https://www.comap-math.com/mcm/2021Certs/21'
for i in range(1, 10000) :
    urlretrieve(mcm + str(i).rjust(5,'0') + '.pdf', root + str(i).rjust(5,'0') + '.pdf')
    
from PyPDF2 import PdfFileMerger

target_path = '/Users/kwsy/Desktop'
pdf_lst = [f for f in os.listdir(root) if f.endswith('.pdf')]
pdf_lst = [os.path.join(root, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

file_merger.write(root + "merge.pdf")
