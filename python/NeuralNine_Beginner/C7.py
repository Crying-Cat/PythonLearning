def sum(*nums,k):
    res = 0
    for num in nums:
        res += num
    return res*k

print(sum(1,2,3,4,5))


