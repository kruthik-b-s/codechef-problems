T = int(input())
if T >= 1 and T <= 1000:
    for i in range(T):
        N, M = map(int, input().split())
        if N >= 0 and N <= 1000:
            if M >= 1 and M <= 1000:
                out = N*M
                print(out)
else:
    print("input out of range")
