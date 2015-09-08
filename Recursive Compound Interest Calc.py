def interest(p, r, i):
    if(i == 0):
        return p;
    else:
        return interest(p*(1+r), r, i-1);
print(str(round(interest(100, 0.1, 12), 2)));