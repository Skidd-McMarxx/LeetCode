class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        start_times = sorted(startTime)
        cache = {}

        def binary_search(times:list[int], target:int):
            lo, hi = 0, len(times)

            while lo < hi:
                mid = (hi + lo) // 2
                if times[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def deep_field_search(index):
            if index == len(jobs):
                return 0
            if index in cache:
                return cache[index]
            
            result = deep_field_search(index + 1)

            next_index = binary_search(start_times, jobs[index][1])
            cache[index] = result = max(result, jobs[index][2] + deep_field_search(next_index))
            return result
        
        return deep_field_search(0)