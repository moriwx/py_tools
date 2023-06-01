import difflib
def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f: text = f.readlines()
    return text

d = difflib.HtmlDiff()
res = d.make_file(readfile('1.py'),
                  readfile('2.py'))

with open('report.html', 'w+') as f: f.write(res)
