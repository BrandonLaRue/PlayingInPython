print ("Please think of a number between 0 and 100!");
low = 0;
high = 100;
mid = (high - low)/2;
guess = 50;
ri = "";

while True:
    print("Is your secret number " + str(guess) + "?");
    ri = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.");
    if (ri == "l"):
        low = guess;
        mid = (high + low)/2;
        guess = mid;
    elif (ri == "h"):
        high = guess;
        mid = (high + low)/2;
        guess = mid;
    elif (ri == "c"):
        print ("Game over. Your secret number was: " + str(guess));
        break;
    else:
        print("Sorry, I did not understand your input.");
        