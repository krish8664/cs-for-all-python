
def uniCode(beg_hex, end_hex):
    ''' print all the characters in block range mentioned between beg_hex and end_hex in the unicode block'''
    for i in xrange(beg_hex, end_hex): #xrange function creates a integer range for the given hex
	print unichr(i), #print all the unicode characters for the integers using the unichr()

def main():
    uniCode(0x0D00, 0x0D7F)

if __name__ == "__main__":
    main()
