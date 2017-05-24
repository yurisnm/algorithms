def waitingTime(tickets, t):

    sorted_tickets = sorted(tickets)
    dp = [0]*(max(tickets)+1)

    for i in range(len(sorted_tickets)-1):
        dp[tickets[i]]+=1

    total = 1
    i = len(dp)-1
    while (t > 0):
        if (dp[i] > 0):
            total += i
            t-=1
            dp[i]-=1
            dp[i - 1]+=1
        else:
            i-=1
    return total