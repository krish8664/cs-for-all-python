
vowels = ['a','e','i','o','u']

def initial_consonants(word):
    ''' find out all the initial consonants in the word recursively and return them, until you 
	find a vowel or the word is null'''
    if not word or word[0] in vowels:
	return ""
    else:
	return word[0] + initial_consonants(word[1:])

def pigLatin(word):
    ''' Converts a word and returns the pigating version of the word
	'''
    if not word:
	return ""
    elif (word[0] in vowels) or (word[0] == "y" and word[1] not in vowels):
	return word + "way"
    else:
	initConsonants = initial_consonants(word)
	return word[len(initConsonants):] + initConsonants + "ay"

def main():
    word = raw_input()
    print pigLatin(word)

if __name__ == "__main__":
    main()
