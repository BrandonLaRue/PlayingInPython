def gcdRecur(a, b):
    g = b / a;
    
    if (b - a * g != 0):
        return gcdRecur(b - a * g , a);
    else:
        return a;


    
