def solve(nh,nl):
    ns='No solution!'
    for i in range(nh+1):
        j=nh-i
        if 2*i+4*j == nl:
            print("No of chickens=",i, "No of rabbits=",j)
            break
    else:
        print(ns)

solve(35,94)