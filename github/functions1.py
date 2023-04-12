import math
from math import exp
from flask import Flask, render_template
from lib.helper import congratsMsg1

###A function with no argument##############
def printFunction():
    print("I am inside printFunction")

###Passing arguments to functions##############
def addIntegers(a,b):
    return a+b

###########User defined functions##############
def addInts():
	num1 = eval(input("Enter number 1: "))
	num2 = eval(input("Enter number 2: "))
	sum = num1 + num2
	print("Sum of two numbers:", sum)

#############built in functions################
def calcExpo(a):
    print('absolute value of 5.25 is:', abs(-5))
    return a*(exp(1e-5) - 1)

####lambda function############################
multResult = lambda a, b : a * b

######Publishing a web page using functions####
app = Flask(__name__)

def getRankingList():
    return 'Congratulations for publishing a web page!'

@app.route('/')
def home():
    try:
        message = getRankingList()
        msg = congratsMsg1()
        return render_template('index.html', message = message, msg = msg)
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    printFunction()
    a = 10
    b = 40
    res = addIntegers(a, b)
    print(a, '+', b, ' result is ',res)
    addInts()
    res = calcExpo(4)
    print('res is:', res)
    res = multResult(5,6)
    print("res is now:", res)
    app.run(debug=True)