"""
Challenge:
Given a sorted array of integers (which may contain both negative and positive values),
rearrange it in ascending order based on the squares of its elements.

Examples:
Input:  [1, 5, 7, 7, 8, 10]
Output: [1, 5, 7, 7, 8, 10]

Input:  [-5, -5, -3, -3, 2, 4, 4, 8]
Output: [2, -3, -3, 4, 4, -5, -5, 8]

Input:  [-10, -8, -7, -7, -5, -1]
Output: [-1, -5, -7, -7, -8, -10]
"""

from typing import List

def sort_by_square(arr: List[int]) -> List[int]:
    """
    Sorts the array in ascending order based on the squares of the elements.
    TODO: Implement the solution.
    """
    # Example using sorted() (simple starting point)
    # return sorted(arr, key=lambda x: x*x)

    # TODO: Replace with two-pointer version or stable version
    # if arr[0] >= 0:
    #     return arr

    ##### THE CASE BELOW IS ONLY WHEN THERE IS NO STABILITY REQUIRED
    # N = len(arr)
    # L,R = 0, N-1
    # result = [0] * N
    # pos = N-1
    # while L <= R:
    #     if abs(arr[L]) > abs(arr[R]):
    #         result[pos] = arr[L]
    #         L+=1
    #     else:
    #         result[pos] = arr[R]
    #         R-=1
    #     pos -=1
    # return result
    
    # neg = [x for x in arr if x < 0][::-1] #needs invert
    # pos = [x for x in arr if x>=0]
    
    # result = []
    # i=j=0
    # while i < len(neg) and j < len(pos):
    #     if abs(neg[i]) <= abs(pos[j]):
    #         result.append(neg[i])
    #         i += 1
    #     else:
    #         result.append(pos[j])
    #         j += 1
    
    # # copy the nums left
    # result.extend(neg[i:])
    # result.extend(pos[j:])
    
    # return result
  
    ### QUADRATIC SOLUTION  
    # result = []
    # temp = list(arr)  # cria uma cópia para não alterar o original
    # n = len(temp)
    
    # # Usamos um "merge" manual percorrendo o array original
    # # Vamos construir uma lista com índices para o merge
    # # Para cada passo, pegamos o menor abs() disponível mantendo a ordem
    # while temp:
    #     # encontra o índice do elemento com menor abs()
    #     min_idx = 0
    #     for i in range(0, len(temp)):
    #         if abs(temp[i]) < abs(temp[min_idx]):
    #             min_idx = i
    #     # adiciona no resultado e remove de temp
    #     result.append(temp[min_idx])
    #     # print(min_idx)
    #     # print(temp)
    #     temp.pop(min_idx)
    #     # print(temp)
    #     # print(result)
    # return result
    
    
    def merge_sort(nums: List[int]) -> List[int]:
        """
        Recursive merge sort function that sorts the list based on absolute value.
        """
        # Base case: an array of size 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums
        
        # Split the array into two halves
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])   # Recursively sort the left half
        right = merge_sort(nums[mid:])  # Recursively sort the right half
        
        # Merge the two sorted halves into one array
        merged = []
        i = j = 0  # Pointers for left and right halves
        
        # Compare elements by absolute value and merge
        while i < len(left) and j < len(right):
            if abs(left[i]) <= abs(right[j]):
                # If abs(left[i]) <= abs(right[j]), choose left[i]
                # This preserves stability: left element goes first if equal
                merged.append(left[i])
                i += 1
            else:
                # Otherwise, choose right[j]
                merged.append(right[j])
                j += 1
        
        # Append any remaining elements from left or right
        # Only one of these two loops will actually add elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
    
    # Call merge_sort on the original array and return the sorted result
    return merge_sort(arr)
    
# ------------------------------
# Test cases
# ------------------------------
if __name__ == "__main__":
    tests = [
        {
            "input": [1, 5, 7, 7, 8, 10],
            "expected": [1, 5, 7, 7, 8, 10],
        },
        {
            "input": [-5, -5, -3, -3, 2, 4, 4, 8],
            "expected": [2, -3, -3, 4, 4, -5, -5, 8],
        },
        {
            "input": [-10, -8, -7, -7, -5, -1],
            "expected": [-1, -5, -7, -7, -8, -10],
        },
         {
            "input": [-5, 5, -3, 3],
            "expected": [-3, 3, -5, 5],  # stability required
        },
    ]

    for i, test in enumerate(tests, 1):
        result = sort_by_square(test["input"].copy())
        print(f"Test {i}: {result} | Expected: {test['expected']} | {'✅' if result == test['expected'] else '❌'}")
