#Q.1- Count even and odd numbers in that list.
l=[]
even,odd=0,0
elements=int(input("Enter the number of elements to be added in list"))
for num in range(elements):
    num=int(input("Enter the value"))
    l.append(num)
for n in l:
    if n%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even count=%d\n Odd count=%d\n" %(even,odd))        
