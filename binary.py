
def divideBy2(decimal):
    ''' Returns the quotient and the reminder of the decimal passed '''
    return decimal/2, decimal%2

def convertToBinary(decimal):
    ''' Reuturns the binary equivalent of the passed decimal, using division by 2 principle '''
    if decimal == 0:
 	return ''
    else:
	quo, rem = divideBy2(decimal)
	return str(convertToBinary(quo)) + str(rem) #append the binary of decimal/2 with the reminder of decimal/2

def main():
    decimal = int(raw_input())
    print convertToBinary(decimal)

if __name__ == "__main__":
    main()
