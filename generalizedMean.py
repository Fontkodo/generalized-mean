
import math

def generalizedMean(x,e):
    '''
    This will return the x'th Generalized Mean of a list of numbers e.
    Both x and the elements of e can be any int or float.
    
    For more information on Generalized Means, you can read more on Wikipedia:
    https://en.wikipedia.org/wiki/Generalized_mean
    '''
    
    #Degenerate case
    
    if len(e)==1:
        return float(e[0])
    
    #Checking for NaN's in e
    
    for n in e:
        if n!=n:
            return float('nan')
    
    #Checking if x is a NaN
    
    if x!=x:
        return float('nan')
    
    #Analytic continuation for zero with negative exponents
    
    if x<=0 and 0 in e:
        return 0.0
    
    #Analytic continuation for Geometric Mean
    
    if abs(x) < 0.00001:
        return math.exp(sum([ math.log(n) for n in e])/float(len(e)))
    
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


def GMtest():
    '''
    This function is used to verify that the generalizedMean function works. Returns nothing.
    '''
    
    print ('Now testing the Generalized Mean...\n')
    
    errorCount=0
    
    print ('Testing standard case...')
    if generalizedMean(1,[1,2,3])==2.0:
        print('OK')
    else:
        print ('Standard case failed!')
        errorCount+=1
    
    print ('Testing Geometric Mean...')
    if generalizedMean(0,[2,8])==4.0:
        print ('OK')
    else:
        print ('Geometric Mean failed!')
        errorCount+=1
    
    print ('Testing infinite exponents...')
    if generalizedMean(float('inf'),[1,2,3,4,5])==5.0:
        print ('Positive OK')
    else:
        print ('Positive infinity failed!')
        errorCount+=1
    if generalizedMean(float('-inf'),[1,2,3,4,5])==1.0:
        print ('Negative OK')
    else:
        print ('Negative infinity failed!')
        errorCount+=1
    
    print ('Testing degenerate case...')
    if generalizedMean(98,[2])==2.0:
        print ('OK')
    else:
        print ('Degenerate case failed!')
        errorCount+=1
    
    print ('Testing NaN finder...')
    if generalizedMean(float('nan'),[9,2])!=generalizedMean(float('nan'),[9,2]):
        print ('Exponent OK')
    else:
        print ('Exponent NaN finder failed!')
        errorCount+=1
    if generalizedMean(5,[7,float('nan')])!=generalizedMean(5,[7,float('nan')]):
        print ('Element OK')
    else:
        print ('Element NaN finder failed!')
        errorCount+=1
    
    print()
    if errorCount!=1:
        print ('You had {} total errors.'.format(errorCount))
    else:
        print ('You had 1 total error.')
    if errorCount==0:
        print ('The function is stable.')
    elif errorCount>0:
        print ('The function is unstable.')
    else:
        print ('Wait, what?')
        print ('How did you do that?')
        print ('You really screwed up this time.')
