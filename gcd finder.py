def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    g = min(a,b);
    while(g > 0):
        if(a % g == 0 and b % g == 0):
            return g;
            break;
        else:
            g -= 1;

   
