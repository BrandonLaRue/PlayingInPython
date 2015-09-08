#P2 Q3

balance = 999999;
annualInterestRate = 0.18;

def calcYear(b, m):
    for i in range(0 , 12):
      
        b -= m;
        b += b * (annualInterestRate/12);
    return b;
    
    
low = balance/12;
up = (balance * (1 + annualInterestRate / 12)**12) / 12



while (True):
    g = (low + up) / 2;
    b = calcYear(balance, g);
    if(abs(b) > 0.01):
        if(b < 0):
            up = g;
        elif(b > 0): 
            low = g;
    else:
        print(str(round(g, 2)));
        break;
        
#End Q3