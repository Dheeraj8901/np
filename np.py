i=int(input())
a=0
b=0
c=0
equation=((a**b)+(b**2)+(a*b)+(b*c)+(c*a))
n=6
f=0
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if (equation)==n:
                print(i,j,k)
                f=1
if f==0:
   print("np") 
   #correct prg 
   