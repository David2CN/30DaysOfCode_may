def bits_of_gray(n):
    """
    This function takes in a positve number, n, and returns a list of the gray codes(The gray code system is a binary number system in which every successive pair of numbers differs in only one bit) for n in order.
    """
    try:
        if type(n) != int or n <= 0:
            raise ValueError
        if n == 1:
            return ["0", "1"]
        else:
            gray_codes = ["0" + i for i in bits_of_gray(n-1)] + ["1" + i for i in reversed(bits_of_gray(n-1))]
            """
            from n = 1, gray_codes = [0, 1]
                     n = 2, gray_codes = [0 + 0, 0 + 1] + [1 + 1 + 1 + 0] 
                                             == [00, 01, 11, 10]
                     n = 3, gray_codes = [0 + 00, 0 + 01, 0 + 11, 0 + 10] + [1 + 10, 1 + 11, 1 + 01, 1 + 00]
                                             == [000, 001, 011, 010, 110, 111, 101, 100]
                     and so on...
            """
            return gray_codes
    except ValueError:
        return "ValueError: n must be a positive integer!!"
     
    
print(bits_of_gray(2))
print(bits_of_gray(3))
print(bits_of_gray(4))
print(bits_of_gray(5))


"""
For example, 

When n = 2, the bits_of_gray function  returns: [00, 01, 11, 10]

When n = 3 , the bits_of_gray function  returns: [ 000, 001,011,010,110,111,101,100]
"""