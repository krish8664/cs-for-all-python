
def swapItems(numList, index, minValueIndex):
    ''' Swar the two elements in the list passed '''
    numList[index], numList[minValueIndex] = numList[minValueIndex], numList[index]

def findMin(numList, index):
    ''' Returns the index of the minimum valued element in the list'''
    minValueIndex = index
    for i in range(index, len(numList)):
	if numList[i] < numList[minValueIndex]:
            minValueIndex = i
    return minValueIndex

def selectionSort(numList):
    ''' Sort the entered list based on selection sort'''
    for index in range(len(numList)):
        minValueIndex = findMin(numList, index)
        swapItems(numList, index, minValueIndex)

if __name__ == "__main__":
    someList = [10,12,3,45,6,78]
    selectionSort(someList)
    print someList
