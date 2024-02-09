def spy_game(str):
    a=0
    b=bool(False)
    for i in range(len(str)):
        if str[i]==0:
            a+=1
        if str[i]==7 and a>1:
            b=True
            break
    print(b)