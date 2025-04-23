def primenumber(MyNum):
    #prime number check
    if MyNum<2:
        return False
    for i in range(2,int(MyNum**0.5)+1):#Only check up to square root of Mynum
        if MyNum %i==0:
            return False
        return True

X=50
print("Prime numbers less than",x,"are:")
for i in range(2,x+1):
    if primenumber(i):#check if i is prime
        print(i,end="")
