# # from sys import maxint
# def maxSubArray(nums):
#     max_so_far = float('-inf') 
#     max_ending_here = 0
      
#     for i in range(0, len(nums)):
#         max_ending_here = max_ending_here + nums[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
 
#         if max_ending_here < 0:
#             max_ending_here = 0  
#     print(max_so_far)
#     return max_so_far

# nums = [5,-1,-6,99]
# maxSubArray(nums)

def maxSubArray(nums):
    max_ = float('-inf')
    max_helper = 0
    
    for num in nums:
        max_helper += num
        max_ = max(max_, max_helper)
        
        if(max_helper < 0):
            max_helper = 0
    print(max_)
    return max_

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])    