# import time


# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         stop_time = time.time()
#         print('run time is %s' % (stop_time-start_time))
#         return res
#     return wrapper


# @timmer
# def foo():
#     time.sleep(3)
#     print('from foo')


# foo()

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = set()
        neg = set()
        for i in nums:
            if i >= 0:
                pos.add(i)
            else:
                neg.add(i)
        print(pos)
        print(len(pos))
        print(neg)
        print(len(neg))

        return len(pos) if len(pos) > len(neg) else len(neg)


if __name__ == "__main__":
    s1 = Solution()
    nums = [-1924, -1910, -1840, -1797, -1714, -1640, -1638, -1567, -1564, -1409, -1141, -1115, -1068, -658, -465, -447, -434, -386, -321, -191, -186, -127, -
            63, 69, 186, 253, 334, 401, 482, 805, 809, 812, 833, 913, 955, 991, 1113, 1128, 1133, 1178, 1204, 1570, 1616, 1725, 1729, 1787, 1853, 1943, 1980, 1980]
    s1.maximumCount(nums)
