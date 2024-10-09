class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(i = 0, partialSum = 0, partial = []):
            if partialSum > target:
                return
            if partialSum == target:
                combinations.append(partial)
 
            for idx in range(i, len(candidates)):
                bt(idx, partialSum+candidates[idx], partial + [candidates[idx]])
        
        combinations = []
        bt()
        return combinations
