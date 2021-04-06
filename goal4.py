import random

numbers=int(input("enter size of unique no-"))
l=[]
for i in range(numbers):
    num=int(input("enter no-"))
    l.append(num)
sffsdfdf
print(l)

def pick(l,numbers):
    while(numbers>0):
        randno=random.choice(l[0:numbers])
        ind=l.index(randno)
        temp=l[ind]
        l[ind]=l[numbers-1]
        l[numbers-1]=temp
        print(randno)
        
       
        numbers=numbers-1    



pick(l,numbers)


#these are my changes
