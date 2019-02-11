number_3 = [10,20,30,40,50,60,70,80,90]
number_5 = []
for n in number_3:
    number_4 = n^3
    # print(number_3)
    number_5.append(number_4)
print(number_5)
number_3 = number_5[:]
print(number_3)
print(number_5)