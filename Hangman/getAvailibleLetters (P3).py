def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    ret = '';
    alpha = "abcdefghijklmnopqrstuvwxyz";
    for l in alpha:
        if(not(l in lettersGuessed)):
            ret += l;
    return ret;
    
