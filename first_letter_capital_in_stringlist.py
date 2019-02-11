
friends = ['arjun', 'ashu', 'nil', 'sumit', 'ganesh', 'spandan', 'tapan']
print(friends)
friends_c = []
for char in friends:
    var = char[0].upper()
    friends_c.append(var + char[1:])
print(friends_c)
