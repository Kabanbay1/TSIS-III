def list_u(list):
    a=0
    list_u=[]
    list_u.append(list[0])
    for i in range(len(list)):
        for j in range(len(list_u)):
            if list_u[j]!=list[i]:
                a+=1
            if a==len(list_u):
                list_u.append(list[i])
        a=0
    return(list_u)