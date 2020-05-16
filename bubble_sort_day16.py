def bubble_sort(array):
    """
    This function takes in an array of integers and sorts the elements of the array  using bubble sort algorithm and returns the number of swaps required to sort the array completely.
    """
    assert type(array) == list and [k for k in array if type(k) != int] == []
    xz = len(array)
    swap_count = 0
    for j in range(xz-1, 0, -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i] , array[i + 1] = array[i + 1], array[i]
                swap_count += 1    
    return swap_count


d = [3, 2, 1, 4]
print(bubble_sort(d))
print(d)

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
c=[9, 10, 6, 2, 3, 5, 4, 8, 7, 1]

print(bubble_sort(a)) #prints 0
print(a) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(bubble_sort(b)) #prints 45
print(b) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

print(bubble_sort(c)) #prints 29
print(c) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]