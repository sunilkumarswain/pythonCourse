####################################
# Lists
####################################
from random import randint

def basicsList():
    L = ['apple','banana','orange']
    L1 = [1,2,3]
    L2 = []
    L3 = [1,2,3,['apple','orange','banana']]
    print('Ist element:', L1[0], L3[3][1])
    if 2 in L1:
        print('2 is present in list')
    num = len(L1)
    print('num of elements is:', num)

def loopingList(list):
    num = len(list)
    for eachLet in range(num):
        if list[eachLet] == 'spam':
            return eachLet + 1

def sortingList():
    L = []
    for i in range(5):
        L.append(randint(1,100))
    print("List now:", L)
    L.sort()
    print("Sorted List:", L)

def slicingList():
    mylist = [1,2,3,4,5,6,7,8]
    print(mylist[0:1])
    print(mylist[1:])
    print(mylist)
    print(mylist[0:5:2])
    print(mylist[-1])

def concatList(list):
    f = []
    f = list + ['ni'] # Concatenation makes a new list too
    f = f + [1,2,3] + ['niit']
    return f

def repeatList(list):
    f = list * 2
    return f

def appendingList(list):
    print (list)
    list.append('NI') # Growing: add object at end of list
    #print list
    return (list)

def shrinkingList(list):
    print(list)
    list.pop(2)
    return list

def reverseList():
    mylist = [2,3,5,7]
    mylist.reverse()
    print(mylist)

def searchItem():
    mylist = [21,5,11,34,28,11]
    item = 11
    index = mylist.index(item)
    print('The index of', item, 'in mylist is:', index)

def countItem():
    mylist = [21,5,11,34,5,28,78,5]
    item = 5
    index = mylist.count(item)
    print('The item', item, 'occurs in mylist:', index, ' many times')

def removeFirstItem():
    mylist = [21,5,11,34,5,28,78,5]
    item = 5
    mylist.remove(item)
    print('mylist now:', mylist)

def removeItemAtIndex():
    mylist = [21,5,11,34,5,28,78,5]
    index = 5
    mylist.pop(index)
    print('mylist now:', mylist)

def insertItemIndex():
    mylist = [21,5,11,34,5,28,78,5]
    index = 5
    item = 66
    mylist.insert(index,item)
    print('mylist now:', mylist)

def inBuiltFunctions():
    mylist = [21,5,11,34,5,28,78,5]
    print(len(mylist), sum(mylist),min(mylist),max(mylist))

if __name__ == '__main__':
    basicsList()
    L = [123, 'spam', 1.23] # A list of three different-type objects
    print (L)
    N = loopingList(L)
    print ('spam happened at:',N)
    mynum = sortingList()
    print('mynum is', mynum)
    s1 = appendingList(L)
    print ('After append:',s1)
    s1 = shrinkingList(L)
    print ('After shrink:', s1)
    slicingList()
    s3 = concatList(L)
    print ('After concatenating:',s3)
    s4 = repeatList(L)
    print ('After repeating:',s4)
    reverseList()
    searchItem()
    countItem()
    removeFirstItem()
    removeItemAtIndex()
    insertItemIndex()
    inBuiltFunctions()