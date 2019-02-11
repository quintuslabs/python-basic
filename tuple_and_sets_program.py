x1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x1)
# x1[0] = 11
months = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december')
print(months)

print(months[7])

man = dict(name='man1', age=20, add='bbsr')
print(man)
print(man.items())

marks = {(100, 50): 'math', (100, 99): 'sanskrit', (100, 80): "Information technology"}
print(marks)
print(marks[(100, 50)])

for mname in months:
    print(mname)
i = 0
while i != (len(months) - 1):
    print(months[i])
    i += 1

x2 = (1, 2, 7, 4, 5, 7, 7, 8, 9)
print(x2.count(7))

print(x2.index(7))

p = tuple({1, 2, 3, 4, 5, 6, })
print(p)

s = {1, 2, 3, 4, 4, 4, 5, 6, 7, 9, 9}
# print(s)
s1 = set({1, 2, 5, 7, 8, 8, 9, 3, 3, 3, 6, 7, 6, })
print(s1)

city = {'bbsr', 'blr', 'ctc', 'ctc', 'bbsr'}

print(set(city))
print(list(set(city)))
city.add('rkl')
print(city)
city.add("bbsr")
print(city)
city.remove('rkl')
print(city)
# print(city.remove('bam'))
print(city)
city.discard('blr')
print(city)

abc = {1, 2, 3, 4, 6, 7, 8, 9, 7, 2, 9, 4, 0}

print(abc)
s7 = set({1, 2, 5, 7, 8, 8, 9, 3, 3, 3, 6, 7, 6 })
s8 = set({7,5,8,9,5,6,6,6,86,8,5,2,1})
print(s7)
print(s7 | s8)
print(s7 & s8)
