


dictionary_1 = { "name": 'sangram', "roll" : 14024, "city" : 'bbsr', "course" : 'MCA'}
print(dictionary_1)

dictionary_2 = dict(product = "laptop", company = "hp", quantity = 70)
print(dictionary_2)
for value in dictionary_1.values():
    print(value)


for value in dictionary_2:
    value = dictionary_2.values()
    print(value)

for k,v in dictionary_1.items():
    print(f"key is {k} value is {v}")



print("quantity" in dictionary_1)
print("name" in dictionary_1)

print("sangram" in dictionary_1.values())
print("sangram" in dictionary_1)
