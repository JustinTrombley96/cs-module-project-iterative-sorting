# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j


        # TO-DO: swap the found smallest element with the first element
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    b = len(arr)
    # Traverse through all array elements
    for i in range(b - 1):
        # Last i elements are already in place
        for j in range(0, b-i-1):

            # traverse the array from 0 to b-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



    return arr


# STRETCH: implement the Count Sort function below
# Requires us to know the "max" value that we'll be sorting
# The maximum was arg was so we could specify the max value
# The total range of data we'll be sorting sits between 0 and maximum

def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr
    
    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:
        maximum = max(arr)
    
    # make a bumch of buckets
    buckets = [0 for i in range(maximum + 1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1

    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i 
            j += 1
            buckets[i] -= 1

    return arr

arr = [1, 4, 5, 6, 3, 2 ,3, 2, 1, 2]
print(count_sort(arr))