def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """
    pass

from typing import List

def smallest_missing_positive_integer(nums: List[int]) -> int:

    
    nums = set(filter(lambda x: x > 0, nums))

    
    if not nums:
        return 1

    
    max_num = max(nums)


    for i in range(1, max_num + 2):
        if i not in nums:
            return i





    



  

