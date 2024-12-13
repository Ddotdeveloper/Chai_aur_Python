

def nums(*args):
    print(args) #tuples 
    sum = 0
    for num in args : 
        sum += num
    return sum

print(nums(1,3,3,4,6))
print(nums(1,2,42,4242,4222,43))