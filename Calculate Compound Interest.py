def CI(pi,rate,time):
    result= pi*(pow((1+rate/100),time))
    return result

p=float(input("Enter Principal"))
r=float(input("Enter Rate"))
t=float(input("Enter time"))

amount=CI(p,r,t)
interest= amount-p
print("Compound amount", amount)
print("Compound Interesr", interest)