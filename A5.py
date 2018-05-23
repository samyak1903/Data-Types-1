#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 
A=[10,23,35,46,58,69,80]
B=[1,4,7,15,18,19,24,28,30]
C=[]
C.extend(A)
C.extend(B)
C.sort()
print(C)
