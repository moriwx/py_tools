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

import img2pdf

p = []
for i in range(1, 130) :
	p.append('E:\\a\\0 (' + str(i) + ').jpg')
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)
with open("E:/b/name.pdf", "wb") as f:
	f.write(img2pdf.convert(p, layout_fun=layout_fun))

from pdf2image import convert_from_path
pages = convert_from_path(r'E:\MCM21\00007.pdf', 100)
for page in pages:
    page.save(r'E:\out.jpg', 'JPEG')
    
from PIL import Image
import os
import pytesseract 

img_path = r'E:\out.jpg'
text=pytesseract.image_to_string(Image.open(img_path),lang='eng')
print(text)
