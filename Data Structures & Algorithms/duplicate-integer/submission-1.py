class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create new set and set it = 0
        hashset = set()
        #loop inside the list
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        