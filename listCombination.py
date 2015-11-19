
def combination(numList):
    ''' Returns the list along with the posssible combinations '''
    if not numList:
	return ""
    if len(numList) == 1:
	return numList
    else:
	listOfCombination = [numList[0]]
	#for every element in the remaining list add the first element to it and also add that element to the list
	for i in combination(numList[1:]):
	    listOfCombination.append(numList[0]+i)
	    listOfCombination.append(i)
	return listOfCombination
	
def converToString(numList):
    ''' Conver the list of int numbers to string '''
    return map(lambda x: str(x), numList)

def main():
    n = int(raw_input()) + 1
    numList = converToString(range(1, n))
    print combination(numList)

if __name__ == "__main__":
    main()
