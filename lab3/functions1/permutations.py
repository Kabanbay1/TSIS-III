def  wPermutations(str):
    from itertools import permutations
    for i in permutations(str):
        print(''.join(i))
