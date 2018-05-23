#Q.1- Create a list with user defined inputs. 
l=[]
elements=int(input("Enter the number of elements to be added in list"))
for num in range(elements):
    num=input("Enter the value")
    l.append(num)
print(l)
