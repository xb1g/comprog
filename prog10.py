import numpy as np
import time

def selsort(mylist):
    for i in range(0, len(mylist)):
        minv = mylist[i]
        minp = i
        for l in range(i, len(mylist)):
            if mylist[l] < minv:
                minv = mylist[l]
                minp = l
        mylist[i], mylist[minp] = mylist[minp], mylist[i]
        #print(mylist) #xxx
    return(mylist)

for i in range(4):


    numbers = np.random.randint(10000*(i+1),size=10000*(i+1))
    start = time.time()
    sorted = selsort(numbers)
    end = time.time()
    print(str(i+1)+"0000 time selsort is:")
    print(end-start)
