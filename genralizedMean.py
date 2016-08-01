import math
def generalizedMean(x,e):
    if len(e)==1:
        return float(e[0])
    if x<=0 and 0 in e:
        return 0.0
    if x==0:
        return math.pow(math.exp(sum([math.log(n) for n in e])),1.0/len(e))
    if x==float('-inf'):
        return float(min(e))
    if x==float('inf'):
        return float(max(e))
    return math.pow(float(sum([n**x for n in e]))/len(e),1.0/x)