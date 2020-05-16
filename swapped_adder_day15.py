def swap(a, b):
    """
    This function takes in 2 variables and swaps their content without the use of temporary variables, tuple comparison or Arithmetic operators. 
    """
    assert type(a) == int and type(b) == int, "Error!"
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def gcd(a, b):
    """
    function to find gcd the Using Euclidian algorithm
    """
    c, d = min(a, b), max(a, b)
    while(c):
        d, c = c, d % c
    return d

def product(array):
    """
    This function multiplies all the terms in an list(array)
    """
    assert type(array) == list, "Error!"
    prod = 1
    for i in array:
        prod *= i
    return prod
    
    
def adder(array):
    """
    This function takes in an array of fractions represented as strings and returns the sum of these fractions as a string with the numerator and denominator in their simplest form.
    """
    ast = [i.split("/")[0] for i in array ] + [i.split("/")[1] for i in array]
    assert [i for i in array if type(i) != str] == [] and [j for j in ast if not j.isdigit()] == [], "Error!"
    xz = len(array)
    numerators = [int(i.split("/")[0]) for i in array]
    denominators =  [int(i.split("/")[1]) for i in array]
    
    denominator = product(denominators) #more like common multiple, not necessarily the LCM
    #standard fraction addition technique
    numerator = 0
    for k in range(xz):
        numerator += (denominator // denominators[k]) * numerators[k]
    
    #divide by gcd to get simplest form
    temp = gcd(numerator, denominator)
    numerator, denominator = numerator // temp, denominator // temp
    
    return str(numerator) + "/" + str(denominator)
    
    

print(adder([ '2/21', '1/9', '8/63']))
print("\n")
print(adder(['1/2','1/3','7/6']))
print(swap(-3, 2))    