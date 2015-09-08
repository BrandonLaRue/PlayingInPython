#PS #2 Q #1

balance = 4842;
annualInterestRate = 0.2;
monthlyPaymentRate = 0.04;
amountPaid = 0;

for i in range(0 , 12):
    print("Month: " + str(i + 1));
    print("Minimum monthly payment: " + str(round(monthlyPaymentRate * balance, 2)));
    amountPaid += (monthlyPaymentRate * balance);
    balance -= (monthlyPaymentRate * balance) ;
    balance += balance * (annualInterestRate/12);
    print("Remaining balance: " + str(round(balance, 2)))
    
print("Total paid: " + str(round(amountPaid, 2)));
print("Remaining balance: " + str(round(balance, 2)));

#End Q1