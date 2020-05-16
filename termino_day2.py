def termino(s):
    """
    This function takes in a string of parentheses and returns the minimum number of parentheses to be removed to make the string valid as an integer(each open parenthesis is closed).
    """
    try:
        if any([i for i in s if i != "(" and i != ")"]):
            raise ValueError
            
        count = 0
        total = len(s)    
        for j in range(total):
            if s[j : j + 2] == "()":
                count += 1            
        difference = total - (count * 2)
        return difference
        
    except ValueError:
        return "The string, s, should contain only opening and closing parentheses, '(' and ')' !!!"
    except:
        raise
    
    
s = input("Enter the string of parentheses: ")
print(termino(s))
    



"""
import re
def termino(s):
    
    #This function takes in a string of parentheses and returns the minimum number of parentheses to be removed to make the string valid as an integer(each open parentheses is closed).
    
    pattern = r"\(\)"
    total = len(s)    
    matches = list(re.findall(pattern, s))
    difference = total - (len(matches) * 2)
    return difference
    
s = "(())"
print(termino(s))
"""