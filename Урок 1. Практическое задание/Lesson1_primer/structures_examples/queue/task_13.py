from task_12 import QueueClass


def hot_potato(names_lst, num):
    queue_obj = QueueClass()
    for name in names_lst:
        queue_obj.to_queue(name)

    while queue_obj.size() > 1:
        for i in range(num):
            queue_obj.to_queue(queue_obj.from_queue())

        queue_obj.from_queue()

    return queue_obj.from_queue()


print(hot_potato(["Вася", "Петя", "Света", "Жанна", "Катя", "Лена"], 7))
