# n = candies
# m = machines
# w = workers
# p = cost for each aquisition

m,w,p,n = map(int, input().split())

def calc_paces(m,w,p,n):
    paces = 1
    candies = m * w
    while(candies<n):
        if candies>=p:
            while candies>=p:
                if m<w: m+=1
                else: w+=1
                candies-=p
            paces += 1
        else:
            paces+=1
            candies+=(m*w)

    return paces


print(calc_paces(m,w,p,n))