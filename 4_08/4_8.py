import re
f = open('input.txt','r')
str = f.read()
f.close()

f_results = re.findall(r'\b([А-Я][а-я]+\s(([А-Я].\s?[А-Я].)|([А-Я][а-я]+\s[А-Я][а-я]+\b)))', str)

names = set([r[0] for r in f_results])

f=open('output.txt','w')
for name in names:
    f.write("%s\n" % name) 
f.close()
