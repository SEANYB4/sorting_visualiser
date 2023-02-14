import random


# QUICK SORT

def quick_sort(nums, low, high):
    if low < high:
        nums, p = partition(nums, low, high)
        nums = quick_sort(nums, low, p-1)
        nums = quick_sort(nums, p + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    j = low
    while j < high:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[i], nums[high] = nums[high], nums[i]

    return nums, i



# BUBBLE SORT


def bubble_sort(nums):

    n = len(nums)
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    return nums


# MERGE SORT


def merge_sort(nums):
    if len(nums)<2:
        return nums

    else:
        mid = len(nums)//2
        first = merge_sort(nums[:mid])
        second = merge_sort(nums[mid:])
        return merge(first, second)

def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    while i < len(first):
        final.append(first[i])
        i += 1

    while j < len(second):
        final.append(second[j])
        j += 1

    return final





def main():

    # QUICKSORT

    print("Beginning Quicksort....")

    arr1 = [random.randrange(0, 11) for i in range(10)]
    print(f"Before: {arr1}")
    answer = quick_sort(arr1, 0, (len(arr1)-1))
    print(f"After: {answer}\n")


    # BUBBLESORT

    print("Beginning Bubblesort....")
    arr2 = [random.randrange(0, 11) for i in range(10)]
    print(f"Before: {arr2}")
    answer = bubble_sort(arr2)
    print(f"After: {answer}\n")



    # MERGESORT

    print("Beginning Mergesort....")
    arr3 = [random.randrange(0, 11) for i in range(10)]
    print(f"Before: {arr3}")
    answer = merge_sort(arr3)
    print(F"After: {answer}\n")





main()





    

