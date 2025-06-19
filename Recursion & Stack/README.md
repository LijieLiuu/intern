Recursion & Stack
=================
  
**Differences between Recursion and Stack**

Recursion is an automated mechanism built on the language runtime’s call stack: each function invocation implicitly creates an activation record on that stack.
In contrast, an explicit stack is a manually constructed LIFO data structure in your code, where you must explicitly call push and pop to save and restore algorithmic state. 
In other words, recursion is automatic, whereas an explicit stack must be managed by the programmer.


Pseudocode for level-order traversal(using stack)
If we need to change the order, we should reverse the values list, rather than appending nodes to next_level in reverse.

```python
# level-order traversal template
def levelOrderTraverse(root):
    # always check whether root empty when dealing tree-related leetcode questions
    
    if root is None:
        return []
    # starting level
    curr_level = [root]
    # complete traversal list initialization
    result = []
    
    # As long as curr_level is not empty, we keep adding its next level’s nodes
    while curr_level:
        next_level = []
        for node in curr_level:
            # add next level nodes
            if node.child1 is not None:
                next_level.append(node.child1)
            if node.child2 is not None:
                next_level.append(node.child2)
            # Note!!! Here for different questions, you probably need to make additional adjustments!!!
            ...
        result.append(curr_level)
        curr_level = next_level

    return result
```

[LeetCode 429] 
如果不是tree那样left和right而是children，那么values要用extend而不是append: next_level.extend(node.children). 
extend 是 Python 列表（list）对象的一个方法，用来把一个可迭代对象（如另一个列表、元组等）中的所有元素，逐个添加到当前列表的末尾。
