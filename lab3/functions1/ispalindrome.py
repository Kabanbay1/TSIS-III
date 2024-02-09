def is_palindrome(str):
    a=len(str)-1
    b=0
    c=True
    while a > b:
        if str[a]!=str[b]:
            c=False
        a-=1
        b+=1
    print(c)