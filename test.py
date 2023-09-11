import math

def reverse():
    response = get_response()
    word = " "
    i = 0
    while i > -(len(response)):
        word += (response[i-1])
        i -= 1
    print(word)

def get_response():
    while True:
        response = input('Enter a word: ')
        if response.isalpha():
            return response
        else:
            print(f"{response} is not a valid response. Please try again")

def three_intergers(a,b,c):
    max = 0
    for i in [a,b,c]:
        if i > max:
            max = i
    print(max)

def recursion(num):
    if num == 0:
        return 1
    else:
        return num * recursion(num -1)


def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num -1) + fib(num-2)