T = int(input())
if T>=1 and T<=1000:
    for i in range(T):
        N, K = map(int, input().split())
        if N>=1 and N<=1000:
            if K>=0 and K<=N:
                S = input()
                NEW_S=[]
                NEW_S[:0]=S
                for q in range(len(NEW_S)):
                    NEW_S[q]=int(NEW_S[q])
                s=NEW_S[::-1]
                a=0
                for a in range(len(NEW_S)):
                    if s[a]!=NEW_S[a]:
                        a=a+1
                print(a)
                print(NEW_S, s)
                # if K==0 and NEW_S==s:
                #     print("YES")
                # elif K==0 and NEW_S!=s:
                #     print("NO")
                # elif K==((a-1)/2) and (a-1)%2==0:
                #     print("Yes")
                # elif K==((a-1)/2) and (a-1)%2!=0:
                #     print("NO")
                # else:
                #     print("NO")
            else:
                print("out of range")
        else:
            print("out of range")       
else:
    print("input out of range")