#P2 Q2

#balance = 3926;
#annualInterestRate = 0.2;
def calcYear(b, m):
    for i in range(0 , 12):
      
        b -= m;
        b += b * (annualInterestRate/12);
    return b;
    
monthly = 0
while(calcYear(balance, monthly) > 0):
    monthly += 10;
   
    
print("Lowest Payment: " + str(monthly));

#End Q2