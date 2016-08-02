def generalizedMean(x,e):
    if len(e)==1:
        return float(e[0])
    for n in e:
        if n!=n:
            return float('nan')
    if x!=x:
        return float('nan')
    if x<0 and 0 in e:
        return 0.0
    if x==0:
        return product(e)**(1.0/len(e))
    if x==float('-inf'):
        return float(min(e))
    if x==float('inf'):
        return float(max(e))
    return (float(sum([n**x for n in e]))/len(e))**(1.0/x)
def product(e):
    p=1
    for i in range(len(e)):
        p*=e[i]
    return p
