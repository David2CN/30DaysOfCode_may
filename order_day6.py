def order(array):
    """
    This function takes in an unsorted array of integers(array) and returns a tuple of 2 elements. The first element is the length of the longest consecutive elements sequence and the second is a sorted list of the remaining elements.
    """
    for i in array:
        assert type(i) == int, "The array should contain only integers!!"      
    #To get all consecutive sequences
    array.sort()
    consecutive, temp = [], []
    for j in range(1, len(array)):
        if array[j] - array[j - 1] == 1:
            temp.append(array[j])
            if array[j - 1] not in temp:
                temp.append(array[j - 1])
        else:
            consecutive.append(temp)
            temp = []
    consecutive.append(temp)
    
    if consecutive == []:
        return (0, array)
    else:
        lengths = []
        for _ in consecutive:
            lengths.append(len(_))
        
        longest = max(lengths)
        xz = lengths.index(longest)
        temp2 = consecutive[xz]
        rest = [i for i in array if i not in temp2]
        return (longest, rest)