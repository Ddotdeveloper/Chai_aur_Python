# age = int(input("Age : \n"))
# day =  input("Day : \n")
# amount_adult = 12
# amount_child = 8
# if age >= 18 : 
#     if day == "Web" : 
#         amount_adult -= 2
#     print("Ticket Price For You is : ",amount_adult,"Have a Nice Day")
# else : 
#      if day == "Web" : 
#         amount_child -= 2
#      print("Ticket Price For You is : ",amount_child,"Have a Nice Day")

# You can Ternery operator for this also 

age = int(input("Age : \n"))
day =  input("Day : \n")
price = 12 if age >= 18 else 8
if day == "Web" :
    price = price - 2 
    print(price)
else : 
    print(price)
