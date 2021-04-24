import os
root = r'E:\\MCM21\\'
mcm = 'https://www.comap-math.com/mcm/2021Certs/21'

# Merge PDFs
from PyPDF2 import PdfFileMerger

pdf_lst = [f for f in os.listdir(root) if f.endswith('.pdf')]
pdf_lst = [os.path.join(root, filename) for filename in pdf_lst]
file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)
file_merger.write(root + "merge.pdf")

# Transfer JPGs to PDF
import img2pdf

p = ['1.jpg', '2.jpg']
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)
with open("new.pdf", "wb") as f:
    f.write(img2pdf.convert(p, layout_fun=layout_fun))

# Transfer PDF to JPG, then recognize the text
from pdf2image import convert_from_path
from PIL import Image
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramFiles\Tesseract-OCR\tesseract.exe'

for i in range(5, 28000) :
    fno = str(i).rjust(5,'0')
    print(i, end='\r', flush=True)
    try : 
        page = convert_from_path(mcm + fno + '.pdf', 90)
        if re.search("Mathematical", pytesseract.image_to_string(page[0], lang='eng')) :
            page[0].save(root + fno + '.jpg', 'JPEG')
    except :
        continue
