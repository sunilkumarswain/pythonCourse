#########################################
# Dictionary
#########################################
def basicsDicts():
    d = {} #empty dictionary
    aDict = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30,'May':31, 'Jun':30, 'Jul':31, 'Aug':31,'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    print(aDict['Mar'], aDict.get('Mar'))
    print(aDict.keys(),aDict.values())

def updatingDict():
    d = {'a':'A','b':'B'}
    d['c'] = 'C'
    print('Updated dict', d)

    aDict = {'a':'A','b':'B'}
    aDict.update({'b': 'C'})
    print('By update', aDict)

    aDict = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30,'May':31, 'Jun':30, 'Jul':31, 'Aug':31,'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    aDict.pop('May')
    print('After popping', aDict)
    aDict.popitem()
    print('After popping', aDict)
    del aDict['Jun']
    print('After deleting', aDict)
    aDict.clear()
    print('After clear', aDict)

def loopingDict(myDict):
    for x in myDict:
        print(x,'values',myDict[x])
    for x in myDict.values():
        print('Value now', x)
    for x, y in myDict.items():
        print('Key values', x, y)

def copyDict(myDict):
    cDict = dict(myDict)
    print(cDict)

if __name__ == '__main__':
    aDict = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30,'May':31, 'Jun':30, 'Jul':31, 'Aug':31,'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    nestedDict = {
    "emp1" : {"name" : "John","year" : 'male'},
    "emp2" : {"name" : "Jhili","year" : 'female'},
    "emp3" : {"name" : "Babar","gender" : 'male'}
    }
    basicsDicts()
    updatingDict()
    loopingDict(aDict)
    copyDict(aDict)
    print(nestedDict["emp2"]["name"])
    

