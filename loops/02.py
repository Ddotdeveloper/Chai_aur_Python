n = int(input("Give the value of n "))
ans = 0
for num in range(1,n+1):
    if(num%2 == 0):
        ans += num

print("The sum of Even Numbers is : ", ans)