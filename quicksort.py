def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

if __name__ == '__main__':
    import time
    from random import randint
    array_length = 10000
    array = [randint(0, array_length) for i in range(array_length)]
    before = time.time()
    sorted_array = quickSort(array)
    after = time.time()
    # print(sorted_array)
    print('quick sort 耗时：', after-before)
    before = time.time()
    array.sort()
    after = time.time()
    # print(array)
    print('python sort 耗时：', after-before)