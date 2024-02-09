movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def is_good(str):
    b=False
    for i in range(len(movies)):
        if str==movies[i]["name"] and movies[i]["imdb"]>5.5:
            b=True
            break
        else:
            b=False
    print(b)
x=input("movie:")
is_good(x)
#2
def better_than_5():
    l=[]
    for i in range(len(movies)):
        if movies[i]["imdb"]>5.5:
            l.append(movies[i])
    print(l)
better_than_5()
#3
def cat(str):
    ml=[]
    for i in range(len(movies)):
        if movies[i]["category"]==str:
            ml.append(movies[i])
    print(ml)
p=input("Category:")
cat(p)
#4
def average(list):
    c=0
    a=0
    for i in range(len(list)):
        c+=list[i]["imdb"]
        a+=1
    print(c/a)
average(movies)
#5
def av_cat(str):
    o=0
    s=0
    for i in range(len(movies)):
        if movies[i]["category"]==str:
            s+=movies[i]["imdb"]
            o+=1
    print(s/o)
j=input("Category")
av_cat(j)