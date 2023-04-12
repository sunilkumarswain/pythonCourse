##########################################
# numbers, strings
##########################################
def numericTypes():
	intx = 1
	inty = 35121254887711
	intz = -3255522
	print(type(intx), type(inty), type(intz))
	floatx = 2e4
	floaty = 1.2E5
	floatz = -3.5e4
	print(type(floatx), type(floaty), type(floatz))
	compx = 1j
	compy = 1+1j
	compz = -2j
	print(type(compx), type(compy), type(compz))

def accessStr():
    sQuote = 'spam'
    print ('single quote string is', sQuote)
    dQuote = "spam"
    print ('double quote string is', dQuote)
    mQuote = 'spam'"spam"
    print (mQuote, sQuote[0], dQuote[3])

def lenStr(strin):
    return len(strin)

def slicingStr(stri):
    myStr = stri[1:5] 
    print(myStr)
    myStr = stri[1:]
    print(myStr)
    myStr = stri[-1]
    print(myStr)
    myStr = stri[-2]
    print(myStr)
    myStr = stri[:2]
    print(myStr)
    myStr = stri[1:5:2]
    print(myStr)

def concatStr(strin1,strin2):
    myStr = strin1 + strin2
    return myStr

def repeatStr():
    str3 = '='*21
    print(str3)

def findStr(stri,se):
    s2 = stri.find(se)
    s3 = stri.find('tt')
    return s2,s3

def replaceStr(pstr):
    s = pstr.replace('n','a')
    return s

def splitStr(stri):
    st = stri.split(':')
    print (st[0],st[1],st[2],st[3],len(st),len(stri))

def upperStr(stri):
    print(stri.upper())
    print(stri.lower())

def countSubstring(string):
	print(string.count('o'))

def digitStr(stri):
    print(stri.isalpha())
    print(stri.isdigit())

def stripStr(stri):
    stri = stri.rstrip()
    return stri

def loopingStr(stri):
    num = len(stri)
    for eachLet in range(num):
        if stri[eachLet] == 'l':
            return eachLet + 1

def revStr(string):
    res = ''
    for i in string:
        res = i + res
    return res

if __name__ == '__main__':
	numericTypes()
	accessStr()
	length = lenStr("Hello")
	print('Length of string:', length)
	slicingStr('Friends')
	str1 = "Hello"
	str2 = "World"
	resStr = concatStr(str1, str2)
	print(resStr)
	repeatStr()
	s1, s2 = findStr("Hello world", "wo")
	print(s1, s2)
	myRes = replaceStr("Roman are very friendly")
	print(myRes)
	check = "aaa:bbb:ccc:ddd"
	splitStr(check)
	upperStr("Hello")
	countSubstring("Hello world john")
	digitStr("Hello world")
	digitStr("4325")
	line = 'aaa,bbb,ccccc,dd\n'
	res = stripStr(line)
	print(res)
	count = loopingStr("Hello")
	print(count)
	resStr = revStr("Hello")
	print(resStr)