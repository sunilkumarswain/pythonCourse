############################################################################
# tuples 
############################################################################
#basics
def tuples():
    T = () #empty tuple
    T = tuple() #also empty tuple
    print(T)
    T = 10,20,30,40  #Tuple is a comma separated values
    print ('printing tuple',T)
    t1 = (0,) #A one-item tuple
    print (t1)

#nested tuples    
def nestedTuples():    
    T = (1, 2,'spam',3, 4) 
    print (T)
    t2 = 0, 'Ni', 1.2, 3, [1,2] 
    print (t2)
    t3 = ('abc', ('def', 'ghi')) 
    print (t3)
    
#accessing tuple elements
def accessTuples():
    T = (1, 2,'spam',3, 4) 
    #T[0] = 3
    print (T[0])    #Index, index of index, slice, length
    t3 = ('abc', ('def', 'ghi')) 
    print ('t3 elements are', t3[0],t3[1],t3[0][0],t3[0][1],t3[0][2],t3[1][0],t3[1][1],t3[1][0][1])
    print(t3[-2])
    T = (1, [2, 3], 4)
    T[1][0] = 'spam'
    print(T)
    x,y,z = 100,23,45
    print ("Value of x y z are now", x, y, z)

#slicing a tuple    
def sliceTuples():
    tuple= ('a','b','c','d','e','f','g','h','i','j')
    print(tuple[0:6])
    print(tuple[1:9:2])
    print(tuple[-1:-5:-1])
    print(tuple[1:])
    print(tuple[:2])
    print(tuple[::2])

#concatenate tuples
def concatTuples(tup):
    t1 = tup + (5, 6)
    return t1

#repeat Tuples
def repeatTuples(tup):
    t2 = tup * 3    # repeat
    return t2

#sort tuple
def sortByLength(words):
    t = []
    for word in words:
        t.append((len(word)))
    print(t)
    t.sort(reverse=True)
    print(t)

#list to tuple conversion
def listToTuple(myList):
    mytuple = tuple(myList)
    print(mytuple)
    tmp = list(mytuple)
    print(tmp)
    
#returning tuple from function
def milesToRun(miniMiles):
   week_1 = miniMiles + 2
   week_2 = miniMiles + 6
   week_3 = miniMiles + 10
   week_4 = miniMiles + 14
   return (week_1, week_2, week_3, week_4)

#using tuple for variable length arguments
def varLengthArgs(tPass):
    res = divmod(*tPass)
    print(res)

#list with tuples
def listWithTuples():
    list1 = [1,2,3]
    string1 = 'xyz'
    t = zip(list1, string1)
    for letter, number in t:
        print(number, letter)
    for index, element in enumerate('yxz'):
        print(index, element)

#Dictionary with tuples
def dictWithTuples():
    d1 = {'a':0, 'b':1, 'c':2}
    for key, val in d1.items():
        print(val, key)
    for index, element in enumerate('bac'):
        print(index, element)

if __name__ == '__main__':
    tuples()
    nestedTuples()
    accessTuples()
    sliceTuples()
    tupl = ('spam',123,'hello')
    t1 = concatTuples(tupl)
    print ('tuple is now',t1)
    t2 = repeatTuples(tupl)
    print ('tuple t2 is now',t2)
    myWords = ['a', 'bcdefgh', 'redi', 'bcd']
    sortByLength(myWords)
    myList = [1,2,3,4]
    listToTuple(myList)
    myTup = milesToRun(2)
    print(myTup)
    nTup = (7,3)
    varLengthArgs(nTup)
    listWithTuples()
    dictWithTuples()