# this solution does not work
from typing import List

nums1 = [1, 3, 5, 9, 10, 11]
nums2 = [2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            search_in, search_with = nums1, nums2
        else:
            search_in, search_with = nums2, nums1

        for num in search_with:
            low = 0
            high = len(search_in) - 1

            while low <= high:
                mid_idx = (low + high) // 2
                mid = search_in[mid_idx]
                
                if low == high:
                    search_in.insert(low + 1, num)
                    break
                elif mid == num:
                    search_in.insert(mid_idx + 1, num)
                    break
                elif mid_idx == 0 and mid > num:
                    search_in.insert(0, num)
                    break
                elif mid_idx == 0 and mid < num:
                    search_in.insert(1, num)
                    break
                if mid < num:
                    low = mid_idx + 1
                elif mid > num:
                    high = mid_idx - 1
        print("search with:", search_with)
        print(search_in)
        length = len(search_in)
        median = (length - 1) // 2
        if length  % 2 == 0:
            print("even!")
            return (search_in[median] + search_in[median+1]) / 2
        else:
            return search_in[median]

        
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))