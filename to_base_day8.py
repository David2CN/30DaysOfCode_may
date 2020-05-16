def to_base(decimal, base):
    """
    This function takes in a number(decimal) in base 10 and returns its value in Binary(2), Quatenary(4), Octal(8) or Hexadecimal(16) form as a string.
    """
    assert type(decimal) == int and base in [2, 4, 8, 16], "Error!"
    bases = {2 : 1, 4 : 2, 8 : 3, 16 : 4}
    hexa = {10 : "a", 11 : "b", 12 : "c", 13 : "d", 14 : "e", 15 : "f"}
    if decimal == 0:
        return 0
    b, converted, c = bases.get(base), "", decimal
    while c >= 1:
        temp = c >> b
        temp2 = c - (temp << b)
        if temp2 > 9:
            temp2 = hexa.get(temp2)
        converted += str(temp2)
        c = temp       
    return converted[ : : -1]