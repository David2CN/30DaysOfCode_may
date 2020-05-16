def counter(item, array):
    """
    This function takes in an item and and array and returns the number of times the item appears in the array.
    """
    count = 0
    for j in array:
        if j == item:
            count += 1
    return count

def wedding_chow(chow):
    """
    This function takes in a string representing supplies available at a wedding(chow) and returns a tuple of two elements.
    The first element is the maximum number of guests that can receive complete chow(rsmfd, rice, stew, meat, fish and drink respectively) and the second element is the leftover chow, arranged in order(rsmfd).
    """
    try:
        if type(chow) != str:
            raise TypeError
            
        temp = ["r", "s", "m", "f", "d"]#valid chow
        if any([i for i in chow if i not in temp]):
            remain = ""
            for k in temp:
                temp2 = counter(k, chow)
                remain += k * temp2
            return (0, remain)
            
        available = [] #numbers of available valid chow in the order, rsmfd.
        for j in temp:
            available.append((counter(j, chow)))
        
        complete_chow = min(available) #number of possible complete chow
        chow_left = list(map(lambda x : x - complete_chow, available)) #numbers of the left_over valid chow in the order  rsmfd.
        
        left_over = ""  #left_over valid chow
        a = 0
        for i in temp:
            left_over += (temp[a] * chow_left[a])
            a += 1
        
        return (complete_chow, left_over)
    except TypeError:
        return "TypeError: Chow should be a string of characters(rsmfd)!!"
        

print(wedding_chow('rsmfdrsmfdrsm'))
print(wedding_chow('fdrsmssrrdr'))
print(wedding_chow('rsdmfRd'))