#Q.2- Add the following list to above created list:
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

l=[]
elements=int(input("Enter the number of elements to be added in list"))
for num in range(elements):
    num=input("Enter the value")
    l.append(num)
l1=['google','apple','facebook','microsoft','tesla']
l.extend(l1)
print(l)
