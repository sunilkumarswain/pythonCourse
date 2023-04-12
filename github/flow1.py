#########################################
# flow control
#############if condition################
def ifCond(var):
    if var > 30:
        return 'pass'

#############if else condition################
def ifElseCond(var):
    if var > 30:
        return 'passed'
    else:
        return 'failed'

#############nested if condition################
def nestedifCond(var):
    if var < 20:
        return 'F'
    elif var > 20 and var <= 30:
        return 'D'
    elif var > 30 and var <= 50:
        return 'B'
    elif var > 50 and var <= 60:
        return 'A'
    elif var > 60 and var <= 100:
        return 'O'
    else:
        return 'Invalid'

#############for loop################
def forLoop(max):
    for i in range(max):
        print('number is:', i)

#############while loop################
def whileLoop(max, val):
    while val > max:
        print('Val is now:', val)
        val -= 1

#############do while loop################
def dowhileLoop(number):
    while True:
        print('number is', int(number))
        if number > 3:
            number -= 1
            continue
        else:
            break


if __name__ == '__main__':
    mark = 10
    result = ifCond(mark)
    if result == 'pass':
        print("Congratulations you passed!!")
    else:
        print("You failed, try your test again!!")
    mark = 40
    result = ifElseCond(mark)
    print("You", result)
    mark = 50
    result = nestedifCond(mark)
    print("result", result)
    forLoop(5)
    whileLoop(5, 10)
    dowhileLoop(1) #whatever number you pass it will be executed once

    