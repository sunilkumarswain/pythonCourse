###########################
# Global vs local
###########################
var = 10

def first():
    print('Inside first() : ', var)

def second():
	var = 20
	print('Inside second() : ', var)

def third():
	global var
	var = 3
	print('Inside third() : ', var)

if __name__ == '__main__':
    print('global origin: ', var)
    first()
    print('global first: ', var)
    second()
    print('global second: ', var)
    third()
    print('global third: ', var)
