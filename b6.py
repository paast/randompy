

def b6(n):
    """Returns n in base-6 as a string"""
    ct = 0
    sum = ''
    N = n
    end = str(n % 6)
    while (N >= 6):
        N /= 6
        ct += 1
    for x in range(ct):
        d = (6 ** int(ct - x))
        y = int(n / d)
        n -= d * y
        sum += str(y)
        
    return(sum + end)