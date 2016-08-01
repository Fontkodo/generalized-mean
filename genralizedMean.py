import math
def generalizedMean(x,e):
    if len(e)==1:
        return float(e[0])
    if x<=0 and 0 in e:
        return 0.0
    if x==0:
        return math.pow(product(e),1.0/len(e))
    if x==float('-inf'):
        return float(min(e))
    if x==float('inf'):
        return float(max(e))
    return math.pow(float(sum([n**x for n in e]))/len(e),1.0/x)
def product(e):
    p=1
    for i in range(len(e)):
        p*=e[i]
    return p
