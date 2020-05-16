def average(s):
    """
    This function takes in a string of integers(s) separated by a single space as input and returns their average.
    """
    try:
        numbers = [int(i) for i in s.split()]
        n = len(numbers)
        total = sum(numbers)      
        return total / n
    except ValueError:
        return "The string(s) should contain only integers"
    except ZeroDivisionError:
        return "The string(s) is empty"
    except:
        raise
        

s = input("Enter the string, the numbers should be separated by a single space\nEnter string: ")
#s = "12 11 2 6 7 10"
print(average(s))