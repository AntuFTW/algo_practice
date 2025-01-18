from numpy import random


'''
Does quicksort but used More memory than needed so not really quicksort


def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array

    pivot = array[-1]  # Pivot is last number in array

    i = -1
    for j in range(length):
        if array[j] < pivot:
            i += 1
            temp = array[j]
            # switch position with temp variable
            array[j] = array[i]
            array[i] = temp
    # switch i+1 pos and pivot at the end
    temp = array[i + 1]
    array[i + 1] = pivot
    array[-1] = temp
    # create left and right arrays
    l_array = array[:i + 1]
    r_array = array[i + 2:]
    quick_sort(l_array)
    quick_sort(r_array)
    array[:len(l_array)] = l_array
    array[len(l_array):] = [pivot] + r_array
    return array
    '''


'''def quick_sort(array, start_i, end_i):
    if end_i <= start_i:
        return

    pivot = array[end_i]  # Pivot is last number in array

    i = start_i - 1
    for j in range(start_i, end_i):
        if array[j] < pivot:
            i += 1
            temp = array[j]
            # switch position with temp variable
            array[j] = array[i]
            array[i] = temp
    # switch i+1 pos and pivot at the end
    temp = array[i + 1]
    array[i + 1] = pivot
    array[end_i] = temp
    # create left and right arrays
    # l_array = array[:i + 1]
    # r_array = array[i + 2:]
    quick_sort(array, start_i, i)  # left side
    # i + 2 because i ends before where the pivot moves to
    quick_sort(array, i+2, end_i)
    array[:len(l_array)] = l_array
    array[len(l_array):] = [pivot] + r_array'''


def quick_sort(array, start, end):
    if end <= start:
        return

    pivot = array[end]
    i = start - 1  # i index starting position is one less than array min
    for j in range(start, end):  # goes to end not end + 1 as j does not need to hit last element
        if array[j] < pivot:
            i += 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    temp = array[i + 1]
    array[i + 1] = pivot
    array[end] = temp

    quick_sort(array, start, i)  # left side sort
    quick_sort(array, i + 2, end)  # right side sort
    # its at i + 2 because at i + 1 is the pivot so i + 2 is where new array starts


if __name__ == '__main__':
    array = [random.randint(10000) for i in range(10000)]
    # array = [3, 2, 5, 11, 4, 6, 3, 2, 1, 5]
    # input for end is index as in range this will be limit and j does not need to hit the end of array as thats where pivot is
    quick_sort(array, 0, len(array) - 1)
    # array = [5, 2, 8, 6, 1]
    print(array)
