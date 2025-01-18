from numpy import random


def merge_sort(array):
    length = len(array)
    if length <= 1:
        return
    left_a = array[0: int(length/2)]
    right_a = array[int(length/2):]
    merge_sort(left_a)
    merge_sort(right_a)
    merged = merge(left_a, right_a, array)
    return merged


def merge(left_a, right_a, array):
    len_left = len(left_a)
    len_right = len(right_a)
    length = len(array)
    l, r, i = 0, 0, 0
    while l < len_left and r < len_right and l + r != length:
        if left_a[l] <= right_a[r]:
            array[i] = left_a[l]
            i += 1
            l += 1
        elif right_a[r] < left_a[l]:
            array[i] = right_a[r]
            i += 1
            r += 1

    if l < len_left:
        array[i:] = left_a[l:]

    if r < len_right:
        array[i:] = right_a[r:]

    return array


if __name__ == '__main__':
    array = [9, 4, 6, 11, 4, 6, 3, 2, 1, 10]
    array = [random.randint(1000) for i in range(100000)]
    print(merge_sort(array))
    print(len(array))
