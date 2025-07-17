Sliding Window
======

Suggested Index Represented Meaning
===
**Left pointer** -> The left-most index that is in the window

**Right pointer** -> The very next index that we are looking into

**The window would look like [left, right)**

Conditions:
===

When to move left pointer? When to move right pointer?

Left:**已经满足了某个条件**，然后为了找到**更优解**（如最短长度）或去除冗余

Right:**没遇到终止情况**，继续扩大window  


**[Edge Case 1]** After right pointer reaches the right-most index, what should we do?

继续收缩窗口（移动 left pointer），直到：

满足更新答案条件	或 left == right，即窗口为空为止  


**[Edge Case 2]** After left pointer reaches right pointer, what should we do?

此时窗口为空（left == right），需要重新开始形成一个新窗口。通常继续**向右移动** right++ 



