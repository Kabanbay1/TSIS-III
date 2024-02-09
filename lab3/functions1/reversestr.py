def reverse_str(str):
    s=str.split(" ")
    s1=""
    i=len(s)
    while i!=0:
        s1=s1+ s[i-1]+" "
        i-=1
    return s1