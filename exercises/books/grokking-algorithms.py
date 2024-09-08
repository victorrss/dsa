# Exercise 4.1 from Grokking Algorithms book by Aditya Y. Bhargava
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

a = 6
b = 6

print(f'Sum of {a} and {b} is {sum([a, b])}')

# Exercise 4.2 from Grokking Algorithms book by Aditya Y. Bhargava
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])
    
list = [1,2,3,4,5,6,7,8,9]
print(f'Counting of the list is {count(list)}')

# Exercise 4.3 from Grokking Algorithms book by Aditya Y. Bhargava
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max
    
list = [9,8,7,6,5,4,3,2,1]
print(f'Max of the list is {max(list)}')


# Exercise 4.4 from Grokking Algorithms book by Aditya Y. Bhargava
def binary_search_recur(array, low, high, target):
    # base case
    if high >= low:
        middle = (high+low)//2
        
        # if the target is in the middle
        if array[middle] == target:
            return middle
            
        # If element is smaller than middle, then it can only be present in left subarray
        if array[middle] > target:
            return binary_search_recur(array, low, middle-1,target)
        else: # else the element can only be present in right subarray
            return binary_search_recur(array, middle+1, high,target)
    else:
        return -1
    
def binary_search(array, target):
    high = len(array)-1
    return binary_search_recur(array, 0, high, target)
    
array = [2,4,6,8,9]

index_of_element = binary_search(array, 80)  
  
if index_of_element != -1:  
    print("Element searched is found at the index ", index_of_element, "of the list")  
else:  
    print("Element searched is not found in the list!")  
    
