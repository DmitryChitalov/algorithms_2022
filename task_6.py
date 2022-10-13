class QueueTaskClass:
    def __init__(self):
        self.basic = []
        self.resolve = []
        self.modific = []


    def to_basic(self, task_id):
        self.basic.insert(0, task_id)

    def to_resolve(self):
        self.resolve.insert(0, self.basic.pop())

    def to_modific(self):
        self.modific.insert(0, self.resolve.pop())

    def modific_to_resolve(self):
        self.resolve.insert(0, self.modific.pop())


if __name__ == '__main__':
    res = QueueTaskClass()
    res.to_basic(1)
    res.to_basic(2)
    res.to_basic(3)
    res.to_basic(4)
    res.to_basic(5)
    print(res.basic)

    res.to_resolve()
    res.to_resolve()
    res.to_resolve()
    res.to_modific()
    res.to_modific()
    res.to_modific()
    res.modific_to_resolve()
    res.modific_to_resolve()

    print(res.basic)
    print(res.resolve)
    print(res.modific)