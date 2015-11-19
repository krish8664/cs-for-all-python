def subset(capacity, items):
    ''' Returns the best possible sum of elements of the list that matches the capacity'''
    if capacity <= 0 or items == []:
        return 0
    elif int(items[0]) > capacity:
        return subset(capacity, items[1:])
    else:
        loseIt = subset(capacity, items[1:])
	useIt = int(items[0]) + subset(capacity - int(items[0]), items[1:])
	return max(useIt, loseIt)

capacity = int(raw_input())
items = raw_input().split(",")
print subset(capacity, items)
