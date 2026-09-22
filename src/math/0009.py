class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    solver = Solution()
    print("Test 1 (121):", solver.isPalindrome(121))  
    print("Test 2 (-121):", solver.isPalindrome(-121)) 
    print("Test 3 (10):", solver.isPalindrome(10))     