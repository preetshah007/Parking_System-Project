l=[]
def func(l):
        s=0
        for i in l:
                if(i%10==0):
                        s+=i
for i in range(5):
        i=int(input("Enter a number: "))
        l.append(i)
func(l)