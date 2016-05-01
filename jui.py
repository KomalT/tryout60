import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
Z = np.random.randint(0,4,size=(6,6))
#print Z
c=0
count=[]
mid_val=[]
t1=[]
N0=N1=N2=N3=0
def update(Z):
    N0=N1=N2=N3=0
    for i in range(4):
        for j in range(4):
            a=Z[i:(i+3),j:(j+3)]
            #print a
            for l in range(3):
                for m in range(3):
                    #print l,m
                    mid_element=a[1,1]
                    if l<>1 or m<>1:
                        if a[l,m]==0:
                            N0+=1
                        elif a[l,m]==1:
                            N1+=1
                        elif a[l,m]==2:
                            N2+=1
                        elif a[l,m]==3:
                            N3+=1
            N=([N0,N1,N2,N3]) 
            mid_val.append(mid_element)
           
            count.append(N)
            N0=N1=N2=N3=0
            print N
    #print count
    #print np.size(count)
    count = np.reshape(count, (16, 4))
    #print count
    c0=count[:,0]
    c1=count[:,1]
    c2=count[:,2]
    c3=count[:,3]
    #print c0
    submat=Z[1:5,1:5]
    #print submat
    submat=submat.ravel()
    #print submat
    
    
    for i in range(16):
        
        if submat[i]==0:
            if  c1[i]>=2 and c2[i]>=1:
                submat[i]=2
            elif c1[i]>0:
                submat[i]=1
            elif c3[i>=1]:
                submat[i]=2
            else:
                submat[i]=submat[i]
                
        if submat[i]==1:
            if c2[i]>=2 and c3[i]>=1:
                submat[i]=3
            else:
                submat[i]=submat[i]
                
        if submat[i]==2:
            if c1[i]<2:
                submat[i]=0
            elif  c3[i]>=1: 
                submat[i]=3
            elif c1[i]==0:
                submat[i]=0
            else:
                submat[i]=submat[i]
          
        if submat[i]==3:
            if c1[i]>=1:
                submat[i]=2
            else:
                submat[i]=submat[i]      
    #print submat   
    submat=np.reshape(submat, (4, 4))
    #print submat
    fig=plt.figure()
    t=plt.imshow(Z)
    #t1.append([t])
    plt.colorbar() 
    Z[1:5,1:5]=submat
    #print Z
    
    #plt.pause(5)
    #plt.show()
    N=np.zeros((16,4))
    N=[]
    count=[]
    return(Z)
Z = np.random.randint(0,4,size=(6,6))
#print Z
plt.imshow(Z)
#plt.colorbar() 
plt.pause(2)
Z1=update(Z)
#print Z1
plt.imshow(Z1)
#plt.colorbar() 
plt.pause(2)
Z2=update(Z1)
#print Z2
plt.imshow(Z2)
#plt.colorbar() 
plt.pause(2)
Z3=update(Z2)
#print Z3
plt.imshow(Z3)


 


