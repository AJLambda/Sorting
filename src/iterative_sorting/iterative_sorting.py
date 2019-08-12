# TO-DO: Complete the selection_sort() function below

# ***Selection Sort*** arrange items from smallest to largest.
# Find the smallest item, put it on the far left side.
# Then, find second smallest and insert it directly to the right of smallest.
# You repeat this process, till items are sorted.

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # Find the smallest item
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Start at range (i + 1) for the next element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# In **Bubble Sort**, we make a series of swaps between adjacent elements,
# gradually moving larger elements towards the end of the array (or _bubbling_ larger elements up).

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # subtract 1 from length of array to end at correct index
    for i in range(0, len(arr) - 1):
        # i becomes the last item in the list after it is sorted, so subtract it
        for j in range(0, len(arr) - 1 - i):
            # comparison - inside the inner loop, compare the item with the item on its right
            # if the item on the left is larger than the item on the right
            if arr[j] > arr[j + 1]:
                # swap (trade places)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr