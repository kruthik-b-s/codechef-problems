from numpy import floor
T = int(input())
if T >= 1 and T <= 12:
    for i in range(T):
        N = int(input())
        if N >= 4 and N <= 15:
            f = (0.143*N)**N
            if (f-floor(f)) < 0.5:
                print(int(floor(f)))
            else:
                print(int(floor(f)+1))
else:
    print("input out of range")
