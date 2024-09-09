#         Big O 
#    Time Complexity
# Best      =>  n log(n)
# Average   =>  n log(n)
# Worst     =>  n^2
#
#   Space Complexity
# Worst     =>  log(n)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lower = [i for i in array[1:] if i <= pivot]
        higher = [i for i in array[1:] if i > pivot]
    return quicksort(lower) + [pivot] + quicksort(higher)

array = [1,5,78,2,6,3,7]
print(f'Sorting {array} using quicksort')
print(f'Array {quicksort(array)} sorted using quicksort')
