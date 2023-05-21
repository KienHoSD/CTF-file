def extended_gcd(a,b):
        x, y = 0, 1
        lastx, lasty= 1, 0
        while b:
            a , (q,b) = b, divmod(a,b)
            x , lastx = lastx - q *x, x
            y , lasty = lasty - q *y, y
        return (lastx,lasty,a)
def chinese_remainder_theorem(items):
    M=1
    for a,m in items:
        M*=m
    result = 0
    for a,m in items:
        M1=M//m
        r,s,d = extended_gcd(m,M1)
        if d != 1:
            M=M//m
            continue
        result+=a*M1*s
    return result%M

x = [(2,5),(3,11),(5,17)]
r = chinese_remainder_theorem(x)
print(r)
