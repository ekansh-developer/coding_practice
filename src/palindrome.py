x=input("enter a string")
y=len(x)
i=0
j=y-1
while j>i:
    if x[i]==x[j]:

        if i+1==j-1:
            print("string is pallindrome")
            break
        if i==j-1:
            print("string is pallindrome")
            break
       # if i==j:
       #     print("string is pallindrome")
        #    break
        i+=1
        j-=1

    else:
       print("string is not pallindrome")
       break


