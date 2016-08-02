def generalizedMean(x,e):
    '''
    This will return the x'th generalized mean of a list of numbers e.
    Both x and the elements of e can be any int or float.
    '''
    #Degenerate case
    if len(e)==1:
        return float(e[0])
    #Checking for NaN's
    for n in e:
        if n!=n:
            return float('nan')
    if x!=x:
        return float('nan')
    #Analytic continuation for zero with negative exponents
    if x<0 and 0 in e:
        return 0.0
    #Analytic continuation for Geometric Mean
    if x==0:
        return product(e)**(1.0/len(e))
    #Analytic continuation for infinite exponents
    if x==float('-inf'):
        return float(min(e))
    if x==float('inf'):
        return float(max(e))
    #General procedure
    return (float(sum([n**x for n in e]))/len(e))**(1.0/x)
def product(e):
    '''
    Product function analogous to the sum() function
    '''
    p=1
    for n in e:
        p*=n
    return p
