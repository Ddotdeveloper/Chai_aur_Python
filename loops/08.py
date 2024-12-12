n = int(input("Give value of n is : \n"))
is_prime = 1
for i in range(2,n):
    if(n%i == 0):
        is_prime = 0
if is_prime == 1 : 
    print("N is Prime")
else :
    print("N is Not Prime")