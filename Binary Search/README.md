Binary Search
=====

Binary Search找是一种在有序序列中通过比较中点元素并每次将搜索区间对半缩小，以快速定位目标值的算法

有两种方法，偏左和偏右，但是两个算法很相似，只是反过来


找靠左的那个:
```python
def find_leftmost(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if left < len(nums) and nums[left] == target:
        return left
    return -1
```

找靠右的那个：
```python
import math

def find_rightmost(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = math.ceil((left + right) / 2)
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    if right >= 0 and nums[right] == target:
        return right
    return -1

```
