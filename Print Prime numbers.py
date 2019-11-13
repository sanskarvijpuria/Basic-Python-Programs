r=int(input("Enter the range"))
for i in range(0,r+1):
    if i>1:
        for b in range (2,i):
            if(i%b)==0:
                break
            else:
                print(i)