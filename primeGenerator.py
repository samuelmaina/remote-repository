

def isPrime(num):
    if num <=1:
        return False
    for factor in range(2,num):
        if num % factor ==0:
            return False
    return True
def generatePrimes(upperBound):
    res=[]
    for i in range(2, upperBound + 1):
        if isPrime(i):
            res.append(i)
    return res

assert generatePrimes(10)[0]==2
assert generatePrimes(10)[1]==3
assert generatePrimes(100)[-2]==89
assert generatePrimes(100)[-1]==97


print(generatePrimes(100))