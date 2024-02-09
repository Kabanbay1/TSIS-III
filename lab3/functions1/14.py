from filterforprime import filter_prime
from histogramm import histogramm
from gramtoounce import gramm_to_ounce
from has33 import has_33
from volume import volume
from uniquelist import list_u
from permutations import wPermutations
from spy import spy_game
from solvep import solve_p
from reversestr import reverse_str
from ispalindrome import is_palindrome
from FtoC import F_to_C
from guess import guess_the_number
#1
g=int(input("gramms: "))
print(gramm_to_ounce(g))
#2
f=int(input("F: "))
print(F_to_C(f))
#3
h=int(input("Heads: "))
l=int(input("Legs: "))
solve_p(l,h)
#4
x=input("List of numbers: ")
print(filter_prime(x))
#5
wPermutations("abc")
#6
s=input("String that you want to reverse: ")
print(reverse_str(s))
#7
has_33([1, 2, 3, 4, 5, 6, 7])
has_33([0, 3, 3, 5])
has_33([0,3, 5, 5 ,6 ,6 , 3])
#8
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
#9
r=int(input("Radius of a sphere: "))
volume(r)
#10
print(list_u([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6,1 ,2 ,2 ,3 ,43, 1,23,12,312,4,12,3,123,123,12,312,3,123,123,123,12,312,3,123,21,34]))
#11
p=input("Word to check: ")
is_palindrome(p)
#12
histogramm([4, 9, 7])
#13
guess_the_number()