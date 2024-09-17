class task_bar:
    def __init__(self):
        self.need_to_do = []
        self.in_work = [] # так же является списком для доработки
        self.already_done = []

    def add_task(self, name_task):
        self.need_to_do.append(name_task)

    def into_need_to_do(self, name_task):
        if name_task in self.in_work:
            self.need_to_do.append(name_task)
            self.in_work.remove(name_task)
        if name_task in self.already_done:
            self.need_to_do.append(name_task)
            self.already_done.remove(name_task)

    def into_in_work(self, name_task):
        if name_task in self.need_to_do:
            self.in_work.append(name_task)
            self.need_to_do.remove(name_task)
        if name_task in self.already_done:
            self.in_work.append(name_task)
            self.already_done.remove(name_task)

    def into_already_done(self, name_task):
        if name_task in self.need_to_do:
            self.already_done.append(name_task)
            self.need_to_do.remove(name_task)
        if name_task in self.in_work:
            self.already_done.append(name_task)
            self.in_work.remove(name_task)


    def show(self):
        return self.need_to_do, self.in_work, self.already_done

tt = task_bar()
print(tt.add_task("task_1"))

print(tt.into_in_work("task_1"))
print(tt.show())

print(tt.into_already_done("task_1"))
print(tt.show())