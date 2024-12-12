# numbers = [1,9,-8,4,3,-7,10,-5,6]
# cnt = 0
# for num in numbers:
#     if num < 0 : 
#         cnt += 1
# print("The Number of positives are is : ", cnt)
n = int(input("Give the value of n"))
ans = 0
for num in range(1,n+1):
    if(num%2 == 0):
        ans += num

print("The sum of Even Numbers is : ", ans)

