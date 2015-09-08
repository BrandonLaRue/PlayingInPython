num = raw_input("What number do you want to find the cube root of? ");
num  = float(num)

test = 0
counter = 0.0


while(test < abs(num)):
    counter += 1
    test = counter**3 
counter -= 1
test = counter**3

while(test < abs(num)):
    counter = counter + 0.1 
    test = counter**3
counter -= 0.1
test = counter**3

while(test < abs(num)):
    counter = counter + 0.01
    test = counter**3
counter -= 0.01
test = counter**3

if(num < 0):
    counter = -counter
print("The answer, approximate to two decimals is " + str(counter));
