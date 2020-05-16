def my_cars(array):
    """
    This function takes in an array(cars) and returns the maximum worth of cars you can get.
    """
    assert type(array) == list and [i for i in array if type(i) == int], "Error!"
    x = len(array)
    if x < 3:
        return 0
    cols, rows = x, x
    worths, mine = [], []
    for j in range(cols):
        temp, temp2 = array[j], array[j]
        temp1, temp3 = [array[j]], [array[j]]
        a, b = j + 2, j - 1
        c, d = j + 3, j - 2
        for k in range(a, rows, 2):
                temp += array[k]
        for m in range(c, rows, 2):                
                temp2 += array[m]
        for l in range(0, b, 2):
                temp += array[l]
        for n in range(0, d, 2):
                temp2 += array[n]
        worths.append(max(temp, temp2))
    
    temp4 = array[rows - 1] + array[0]
    for p in range(2, rows-2, 2):
        temp4 += array[p]
    worths.append(temp4)    
    return max(worths)