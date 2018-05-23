#Q.6-Implement a stack and queue using lists.
choice=input("Enter 1 for stack and 2 for queue")
#Stack
if choice=='1':
    print("Stack")
    l=[]
    ch='y'
    while ch.lower()=='y':
        ch1=input("Enter 1 for push and 2 for pop element from the stack")
        if ch1=='1':
            element=input("Enter the element")
            l.append(element)
        elif ch1=='2':
            if len(l)==0:
                print("Stack is empty")
                break
            l.pop()
        else:
            print("Wrong choice")
            break
        print("Stack=",l)
        ch=input("Continue stack? y/n:")
#Queue        
elif choice=='2':
    print("Implementing Queue")
    l1=[]
    ch='y'
    while ch.lower()=='y':
        ch1=input("Enter 1 for insertion and 2 for deletion from queue")
        if ch1=="1":
            element=input("Enter the element")
            l1.append(element)
        elif ch1=="2":
            if len(l1)==0:
                print("Queue is empty")
                break
            l1.pop(0)
        else:
            print("Wrong choice")
            break
        print("Queue=",l1)
        ch=input("Continue stack? y/n:")
        
        
        
        
                 
        
