def distance(first, second):
    ''' Rerturns the minimum edit distance between two strings '''
    if not first:
	return len(second)
    elif not second:
	return len(first)
    elif first[0] == second[0]:
	return distance(first[1:], second[1:])
    else:
	replace = 1 + distance(first[1:], second[1:])
	insertion = 1 + distance(first, second[1:])
	deletion = 1 + distance(first[1:], second)
	return min(replace, insertion, deletion)

print distance(raw_input(), raw_input()) 
