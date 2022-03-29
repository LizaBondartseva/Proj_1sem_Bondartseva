# Практическая №14
# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с корректными номерами телефонов (т.е. в
# номере должно быть 11 цифр, например, 86532547991), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в кадом файле
import re
r = re.compile(r"\d")
t = re.compile(r"\d+-\d+")
g, p = [], []
for o in open('hotline.txt').read().split('\n'):
    p.append(t.findall(o))
    if len(r.findall(o)) == 11:
        g.append(r.findall(o))
    elif len(r.findall(o)) != 11:
        p.append(r.findall(o))
g, p = list(filter(None, g)), list(filter(None, p))
a, b = open('correct.txt', 'w'), open('incorrect.txt', 'w')
for i in g:
    print(''.join(i), sep='\n', file=a)
for i in p:
    print(''.join(i), sep='\n', file=b)
print('Корректных номеров:', len(g), '\n' + 'Некорректных номеров:', len(p))