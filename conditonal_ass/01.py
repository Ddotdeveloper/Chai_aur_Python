age = int(input("User age : \n"))
if age < 13 : 
    print("child\n")
elif age >=13 and age <= 19 :
    print("Teenager \n")
elif age >= 20 and age <= 59 :
    print("adult\n")
else :
    print("Senior\n")
