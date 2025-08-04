# Trie Tree

用**终止符** `$` 来表示一个单词结束了。

**Example:** 将 `["cat", "cap", "car"]` 插入 Trie 后，内部字典可以这样写：

```python
{
  'c': {
    'a': {
      't': {'$': True},   # cat
      'p': {'$': True},   # cap
      'r': {'$': True},   # car
    }
  }
}
```

对应的树形结构：

```
    c
    |
    a
  / | \
 t  p  r
 |  |  |
 $  $  $
```

代碼
===
```python
trie = {}

def insert(root, word):
    node = root
    for ch in word:
        # 如果当前节点没有 ch 这个子节点，就先创建一个空字典
        if ch not in node:
            node[ch] = {}
        # 然后把 node 指向子节点，继续下一轮
        node = node[ch]
    # 最后标记结束符
    node['$'] = True

# 测试插入
for w in ["cat", "cap", "car"]:
    insert(trie, w)
```
