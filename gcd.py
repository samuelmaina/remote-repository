def gcd(nums=[]):
    if len(nums) == 0:
        return 1
    bound= min(nums)
    ans= float("-inf")
    for divisor in range(2, bound+1):
        doAllDivide= True
        for num in nums:
            if(num%divisor != 0):
                doAllDivide= False
                break
        if(doAllDivide):
            ans= max(ans,divisor)
    return ans
print(gcd([4,8,16,32]))
print(gcd([42,63,84]))