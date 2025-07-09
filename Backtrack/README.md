Backtrack
==================

Steps for Backtrack:

Backtrack (by nature, it’s actually DFS)
1. Initialize a global list/dict to store final answer(s)
2. Design a **recursive function** that tries the following step
    a. Continuously recurse until it find an answer or failed a check
    b.Whenever it hits the end condition, it will go back to the previous recursion level to search for the next available option
3.	Return the final global list/dict


```python
results = []

def backtrack(path, options):
    if check_end_condition(path):  # check if it's valid
        return

    if find_an_answer(path):      # check if we have found an answer
        results.append(path[:])
        return

    for option in options:        # explore branches
        if is_valid(option, path):
            path.append(option)
            backtrack(path, options)
            path.pop()            # backtrack!

def solve():
    initial_path = []
    backtrack(initial_path, get_options())
    return results
```



Common Mistakes:
===============
1. Program consistency, the variables representing the same object should have
values from the same state.
2. Deep copy only when the object is finalized
3. Duplicate result: repetitively visiting the parameters

4. A common mistake in backtrack is repeatedly counting solution or traversing the same position/condition/state more than once. 

   A good habit is to create a structured level/order for traversal. Usually used order - array index, grid row/column, etc.

