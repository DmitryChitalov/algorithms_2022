import timeit, collections

ll = []
dd = collections.deque()


def list_test():
    ll.append("a")
    ll.pop(0)
    ll.extend("b")
    ll.insert(0, "c")
    ll.pop(0)
    ll.extend("c")
    print(ll[-1])


def deque_test():
    dd.append("a")
    dd.pop()
    dd.extend("b")
    dd.appendleft("c")
    dd.popleft()
    dd.extendleft("d")
    print(dd[-1])


one = timeit.timeit("list_test()", setup="from __main__ import list_test", number=1000)
two = timeit.timeit("deque_test()", setup="from __main__ import deque_test", number=1000)
print(one)
print(two)
