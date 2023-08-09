class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # tmp = []
        # counter = 0
        # for i in range(len(intervals)):
        #     for j in range(i + 1, len(intervals)):
        #         if intervals[i][0] >= intervals[j][1]:
        #             counter = counter + 1
        #         elif intervals[i][0] == intervals[j][0] and intervals[i][1] == intervals[j][1]:
        #             counter = counter + 1
        # return counter
        intervals.sort()
        print(intervals)
        