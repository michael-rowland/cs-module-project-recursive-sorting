# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    counter_A = 0
    counter_B = 0
    while counter_A + counter_B < elements:
        if counter_A > len(arrA) - 1:
            merged_arr[counter_A+counter_B] = arrB[counter_B]
            counter_B += 1
        elif counter_B > len(arrB) - 1:
            merged_arr[counter_A+counter_B] = arrA[counter_A]
            counter_A += 1
        elif arrA[counter_A] <= arrB[counter_B]:
            merged_arr[counter_A+counter_B] = arrA[counter_A]
            counter_A += 1
        else:
            merged_arr[counter_A+counter_B] = arrB[counter_B]
            counter_B += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return merge([arr[0]], [arr[1]])
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass