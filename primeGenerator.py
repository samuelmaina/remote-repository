import math

def isPrime(num):
    if num <=1:
        return False
    bound= int(math.sqrt(num))
    for factor in range(2,bound):
        if num % factor ==0:
            return False
    return True
def generatePrimes(upperBound):
    res=[]
    for i in range(2, upperBound + 1):
        if isPrime(i):
            res.append(i)
    return res



print(generatePrimes(100))