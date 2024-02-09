def solve_p(leg, head):
    r=(leg-2*head)/2
    c=head-r
    if r <0 or c<0 or leg<0 or head <0:
        print("Error")
    else:
        print("Rabbits:"+str(r)+"\n"+"Chikens:"+str(c))