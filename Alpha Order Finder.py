'''
Goal: find the longest substring of alphabetical characters
'''

#string to be tested:
s = 'azcbobobegghakl'


def isAlpha(x, y, s):
    '''
    x: int (First Character Index)
    y: int (Second Character Index)
    s: str (String Refrenced by Index Values)    
    '''
    
    alpha = "abcdefghijklmnopqrstuvwxyz";
    
    if(alpha.find(s[x]) <= alpha.find(s[y])):
        return True;
    else:
        return False;


def genString(s):
    '''
    s: The String to be Sequenced
    
    This function outputs a binary (t/f) sequence that will show whether the sequence is alphabetical.
    '''
    out = ""    
    for ind in range(0, len(s)-1):
        
        if(isAlpha(ind, ind + 1, s)):
            out += 't';
        elif(not(isAlpha(ind, ind + 1, s))):
                out += 'f';
                
    return out;
    
    
def findSq (s):
    '''
    Uses the output from genString to find alphabetical sequences
    '''
    bestIndex = 0;
    bestLen = 0;

    count = 0;
    sO = s;
    s = genString(s) + 'f';
    for i in range(0, len(s)): 
        if (s[i] == 't'):
            count += 1
        else: 
            if(count > bestLen):
                bestLen = count;
                bestIndex = i - count;
                count = 0;
            else:
                count = 0;
    bestLen += 1;
    return(sO[bestIndex : bestIndex + bestLen]);  
                

print("Longest substring in alphabetical order is: " + findSq(s));