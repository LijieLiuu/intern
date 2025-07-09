class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """

        def helper(dis):
            count = 0
            for i in range(1, len(stations)):
                dist = stations[i] - stations[i - 1]
                count += int(math.ceil(dist / dis)) - 1
            return count <= k

        left, right = 0, stations[-1] - stations[0]
        gap = 1e-6

        while right - left > gap:
            mid = (left + right) / 2.0
            if helper(mid):
                right = mid
            else:
                left = mid
        return left

