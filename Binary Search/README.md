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


Value-based binary search:
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)  # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

What does the **condition** represents as below?

Test whether x meets the goal.


When existing the while loop, what 2 conditions might the left index become?

If a solution exists, left is the **minimal** x with **condition(x)==True**.

Otherwise, left ends up at the boundary, signalling “no valid x found.”

