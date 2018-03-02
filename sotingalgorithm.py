from random import randrange

def createRandomList(n):
    myarray = []
    durum = 0
    for i in range(n):
        foo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
        random_index = randrange(0,len(foo))
        for i in range (0, len(myarray)):
            if(myarray[i]==random_index):
                durum = 1
        if (durum !=1):
            myarray.append(foo[random_index])
        durum =0
    return myarray

def bubbleSort(alist):
    step=0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            step=step+1
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    print(step)
def insertionSort(alist):
   step=0
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
         step=step+1
     alist[position]=currentvalue
   print(step)
newArray = createRandomList(20)
print("----------bubbleSort----------------")
print("----------old list -------------")
print(newArray)
print("----------new list -------------\n")
bubbleSort(newArray)
print(newArray)

newArray = createRandomList(20)
print("----------insertionSort----------------")
print("----------old list -------------")
print(newArray)
print("----------new list -------------")
insertionSort(newArray)
print(newArray)
