class Solution:
    def climbStairs(self, n: int) -> int:
        two_step, one_step = 1, 1
        for _ in range(n-1):
            temp = two_step
            two_step += one_step
            one_step = temp
        return two_step
    

