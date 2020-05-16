def itos(integer):
    """
    This function takes in an integer and returns the value as a string.
    """
    try:
        if type(integer) != int:
            raise ValueError
        string = "{}".format(integer)    
        return string
    except:
        return "ValueError: Please enter an integer value!!"

 
def stoi(string):
    """
    This function takes in a string and returns the value as an integer.
    """
    try:
        if type(string) != str:
            raise ValueError        
        integer = eval(string)
        if type(integer) != int:
            raise ValueError
        return integer
    except ValueError:
        return "ValueError: Please enter a string!!"
    
                        
def ftos(floats):
    """
    This function takes in a float and returns the float converted to a string.
    """
    try:
        if type(floats) != float:
            raise ValueError            
        string = "{}".format(floats)
        return string 
    except ValueError:
        return "ValueError: Please enter a float value!!"

        
def stof(string):
    """
    This function takes in a string and returns the string converted to a float.
    """
    try:
        if type(string) != str:
            raise ValueError
        floats = eval(string)
        if type(floats) != float:
            raise ValueError
        return floats
    except ValueError:
        return "ValueError: Please enter a string!!"


print(ftos(6.669))
print(stoi("11"))
print(stof("12.34"))
print(itos(123))
print(ftos(24.12))