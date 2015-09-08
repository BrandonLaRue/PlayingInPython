def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    g = len(aStr) / 2
    if (len(aStr) <= 1 and aStr != char):
        return False;
    elif (len(aStr) <= 1 and aStr == char):
        return True;
    else:
        if (aStr[g] == char):
            return True;
        elif(char > aStr[g]):
            
            return isIn(char, aStr[g:]);
            
        elif(char < aStr[g]):
             
              return isIn(char, aStr[:g]);         
            
