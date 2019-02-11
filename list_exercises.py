print([bool(val) for val in ([], 0, '')])

numbers_test = [1,2,3,4,5,6,7,8,9]
numbers_test1 = []
print(numbers_test)

for n in numbers_test:
    numbers_test11 = str(numbers_test[n-1])
    numbers_test1.append(numbers_test11)

print(numbers_test1)




num_list = [1,2,3,4,5,6,7,8,9]
num_list2 = [str(num) for num in num_list]
print(num_list2)

numbers_test2 = [1,2,3,4,5,6,7,8,9]
print([num if num % 2 == 0 else num/2 for num in numbers_test2])



lis_1 = [1,2,3,4,5,6]
print(lis_1.count(2))
print(len(lis_1))

