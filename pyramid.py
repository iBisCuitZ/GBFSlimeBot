x=int(input("xd :"))
y=x
z=x
for x in range (1,x+1):
    print(" "*(y-x)+"x"*x+"x"*(x-1))
for x in range (1,x):
    print(" "*abs(y-z+1)+"x"*(z-1)+"x"*(z-2))
    z-=1