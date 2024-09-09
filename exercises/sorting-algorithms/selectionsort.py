#         Big O 
#    Time Complexity
# Best      =>  n^2
# Average   =>  n^2
# Worst     =>  n^2
#
#   Space Complexity
# Worst     =>  O(1)
def selectionsort(array):
    if len(array) < 2:
        return array

    for i in range(len(array)):
        lower = i
        for j in range(i+1,len(array)):
            if array[j] < array[lower]:
                lower = j
                
        if lower != i:
            aux = array[i]
            array[i] = array[lower]
            array[lower] = aux
    return array
    
array = [1,5,78,2,6,3,7]
print(f'Sorting {array} using selection sort')
print(f'Array {selectionsort(array)} sorted using selection sort')
