def filter_prime(list):
    l1=list.split(" ")
    n=[]
    for i in range(len(l1)):
        a=0
        x=0
        while x<int(l1[i]):
            x+=1
            if int(l1[i])%x==0:
                a+=1
        if a==2 or int(l1[i])==1:
            n.append(l1[i])
    return n