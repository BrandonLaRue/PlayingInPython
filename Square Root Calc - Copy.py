num = raw_input("Enter the number you wish to find the square root of: ");
num = float(num);

g = raw_input("Enter your best guess: ");
g = float(g);

error = raw_input("Enter your margin of error (A Percent): ");
error = (float(error)/100);

tempG = g * g;

loop = True;

while(loop):
    
    tempG = g*g;
    if(tempG == num or abs(num - tempG) < (num * error)):
        loop = False;
        print(str(g) + " is the answer.");
    
    else:
        g = g - (tempG - num)/2
    
