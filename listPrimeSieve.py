
def sift(divisorToRemove, numberList):
    ''' Rerns a list after removing all the numbers that are divisible by the divisor
        '''
    return filter(lambda x: x % divisorToRemove != 0, numberList)

def primeSieve(numberList):
    ''' Returns a list of prime numbers after removing all the non prime numbers
        '''
    if not numberList:
        return []
    else:
        prime = numberList[0]
        return [prime] + primeSieve(sift(prime, numberList[1:]))

if __name__ == "__main__":
    n = int(raw_input())
    print primeSieve(range(2, n))    
