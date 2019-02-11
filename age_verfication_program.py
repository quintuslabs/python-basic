age = input(" WELCOME TO THE PVR CINEPLEX ..PLEASE ENTER THE AGE !! \n ")
age = int(age)
print(type(age))
if age > 2 and age < 10:
    print("your ticket is child price \n ")
elif age > 10 :
    print("your ticket is adult price \n ")
else:
    print("your ticket is free \n ")
