class DeskClass:
    def __init__(self):
        self.task = []
        self.correct = []
        self.solved = []

    def is_empty(self):
        return self.task == []

    def to_task(self, item):
        self.task.insert(0, item)

    def from_task(self):
        return self.task.pop()

    def to_correct(self, item):
        self.correct.insert(0, item)

    def from_correct(self):
        return self.correct.pop()

    def to_solved(self, item):
        self.solved.insert(0, item)

    def from_solved(self):
        return self.solved.pop()

    def size(self):
        return len(self.task)

    def size_correct(self):
        return len(self.correct)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_task('my_obj')
    qc_obj.to_task(4)
    qc_obj.to_task(True)

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size())  # -> 3

    print(qc_obj.from_task())  # -> my_obj

    print(qc_obj.size())  # -> 2