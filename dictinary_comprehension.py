numbers_dicti = dict(first = 1, second = 2, third = 3)
squared_dicti = {key:value **2 for key,value in numbers_dicti.items()}
print(squared_dicti)


print({nummm:nummm **2 for nummm in [1,2,3,4,5]})

str1 = "ABC"
str2 = "123"
print({str1[i]:str2[i] for i in range(0,len(str1))})


std_dict = {'std1':'sangram','std2':'saswat','std3':'arjun','std4':'sumit','std5':'susmita'}
print( {k.upper():v.upper() for k,v in std_dict.items()})

num_list = [10,20,355,0,8,60,5,63,26,0,499,144,84]
print({num:("even" if num % 2 == 0 else "odd") for num in num_list})

print({num:("even"  if num % 2 == 0  else "odd") for num in range(0, 100)})
