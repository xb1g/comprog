# read nasdaq.txt

def nasdaq():
    # open file
    infile = open('nasdaq.txt', 'r')
    stocks = infile.readlines()
    infile.close()
    # find the stock with the most percentage change

    hc = 0
    hstock = ""
    for stock in stocks:
        change = float(stock.split()[-1][:-1].replace("-", ""))
        if change > hc:
            hc = change
            hstock = stock


    print(hstock)

    # print(list(map(lambda x: x.split()[-1],stocks)))

    # map(lambda stock: print(stock[-1]), stocks)


nasdaq()
# Output:
import random

secret_number = random.randint(1, 100)
guess = None

print("Welcome to the Guess the Number game!")

while guess != secret_number and guess != 0:
    guess = int(input("Enter your guess (enter 0 to give up): "))
    if guess == 0:
        print("The number was:", secret_number)
        print("Better luck next time!")
        break
    print("The number is higher." if guess < secret_number else "The number is lower.")
print("Congratulations! You guessed the number correctly!" if guess == secret_number else "")

def selsort(mylist):
    for i in range(0, len(mylist)):
        minv = mylist[i]
        minp = i
        for l in range(i, len(mylist)):
            if mylist[l] < minv:
                minv = mylist[l]
                minp = l
        mylist[i], mylist[minp] = mylist[minp], mylist[i]
        print(mylist) #xxx
    return(mylist)

selsort(["x","bunny","car","house"])

"""
['bunny', 'x', 'car', 'house']
['bunny', 'car', 'x', 'house']
['bunny', 'car', 'house', 'x']
['bunny', 'car', 'house', 'x']
"""