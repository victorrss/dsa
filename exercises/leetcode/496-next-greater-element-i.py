class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        nums2Idx = {}
        
        for i in range(len(nums2)):
            nums2Idx[nums2[i]] = i

        for i in range(len(nums1)):
            # search the index of the nums1 element in nums2Idx dict
            # if there is no nums1 correspondent key in it, then it's -1 value
            if nums1[i] not in nums2Idx:
                array.append(-1)
                continue
                
            # search the next greater element from the nums1 element
            # if not found, so it's -1 value
            greater = -1
            for j in range(nums2Idx[nums1[i]], len(nums2)):
                if nums2[j] > nums1[i]:
                    greater = nums2[j]
                    break
                    
            array.append(greater)
            
        return array
