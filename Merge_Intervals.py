# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         # sort intervals in order of first element of each interval
#         intervals.sort(key = lambda x : x[0])
        
#         # curr_start = intervals[0][0]
#         # curr_end = intervals[0][1]
#         new_intervals = []
#         prev_interval = intervals[0]
#         if len(intervals) <= 1:
#             return intervals
#         for i in range(1, len(intervals)):
#             # start = interval[0]
#             # end = interval[1]
#             current_interval = intervals[i]
#             if prev_interval[1] >= current_interval[0]:
#                 new_intervals.append([prev_interval[0], max(prev_interval[1],current_interval[1])])
#                 prev_interval = [prev_interval[0], max(prev_interval[1],current_interval[1])]
#                 continue
#             else:
#                 # new_intervals.append(prev_interval)
#                 if (len(intervals) == 2):             
#                     new_intervals.append(prev_interval)
#                     new_intervals.append(current_interval)
#                 if current_interval[0] > new_intervals[-1][1]:
#                     new_intervals.append(current_interval)
#                 prev_interval = current_interval
#                 continue

#             # curr_start = start
#             # curr_end = end

#         return new_intervals
# solution = Solution()
# print(solution.merge([[0,2],[1,4],[3,5]]))


[[0,2],[1,4],[3,5]]


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x : x[0])
        
        prev_interval = intervals[0]
        new_intervals = []
        new_intervals.append(prev_interval)
        for i in range(len(intervals)):
            cur_interval = intervals[i]
            if prev_interval[1] >= cur_interval[0]:
                new_intervals.pop(-1)
                new_intervals.append([prev_interval[0], max(prev_interval[1], cur_interval[1])])
                prev_interval = new_intervals[-1]
                continue
            else:
                new_intervals.append(cur_interval)
                prev_interval = cur_interval
                continue
        
        return new_intervals
                
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))