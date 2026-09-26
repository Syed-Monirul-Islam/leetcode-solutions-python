from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

if __name__ == "__main__":
    solver = Solution()
    print("Test 1:", solver.containsDuplicate([1, 2, 3, 1])) 
    print("Test 2:", solver.containsDuplicate([1, 2, 3, 4])) 