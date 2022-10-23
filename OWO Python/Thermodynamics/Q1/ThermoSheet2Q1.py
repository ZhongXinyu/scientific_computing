
N=4 #number of oscillators
m=5 #number of quantas
g=[0]*N

def enumerate(N,m,g,counter):
    if N == 1:
        g[N-1]=m
        counter +=1
        #print (counter,g)
        return 1,counter
    elif m == 0:
        g[0:N]=[0]*N
        counter +=1
        #print (counter,g)
        return 1,counter
    else:
        sum=0
        for i in range (0,m+1):
            g[N-1]=i
            sum0,counter = enumerate(N-1,m-i,g,counter)
            sum=sum+sum0
    return sum,counter

enumerate (N,m,g,0)

#Part (b)
print ("Quanta","4-Osci","2-Osci",sep="\t")
for m in range (0,6):
    print (f"m={m}:",enumerate (4,m,[0]*4,0)[0],enumerate (2,m,[0]*2,0)[0],sep='\t')
