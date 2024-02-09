def has_33(str):
    b=bool(False)
    for i in range(len(str)):
        if i<len(str)-1:
            if str[i]==3 and str[i+1]==3:
                b=True
                break
    print(b)