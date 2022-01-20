class Problems:
    def __init__(self):
        self.problems = []
        self.solved = []
        self.solve_later = []
        self.max_queue_index = 1

    def solve(self, queue_index):
        for i in range(len(self.problems)):
            if self.problems[i][1] == queue_index:
                self.solved.append(self.problems[i][0])
                self.max_queue_index -= 1
                self.problems.pop(i)
                for l in range(len(self.problems)):
                    self.problems[l][1] = l + 1
                break
    def resolve(self, queue_index):
        for i in range(len(self.problems)):
            if self.problems[i][1] == queue_index:
                self.solve_later.append(self.problems[i][0])
                self.max_queue_index -= 1
                self.problems.pop(i)
                for l in range(len(self.problems)):
                    self.problems[l][1] = l + 1
                break

    def quantity(self):
        return f'queued: {len(self.problems)}. \nsolve later: {len(self.solve_later)}'

    def is_queue_empty(self):
        return self.problems == []

    def add_problem(self, description):
        self.problems.append([description, self.max_queue_index])
        self.max_queue_index += 1

    def show_problems(self):
        print(f"already solved: {self.solved}")
        print(f"solve later: {self.solve_later}")
        print(f"currently queued: {[i[0] for i in self.problems]}")

problem_stack = Problems()
problem_stack.is_queue_empty()
problem_stack.add_problem('task#1')
problem_stack.add_problem('task#2')
problem_stack.add_problem('task#3')
problem_stack.add_problem('task#4')
problem_stack.add_problem('task#5')
problem_stack.add_problem('task#6')
print(problem_stack.problems)
problem_stack.solve(1)
problem_stack.resolve(3)
problem_stack.resolve(4)
problem_stack.solve(2)
problem_stack.is_queue_empty()
print(problem_stack.problems)
print(problem_stack.solved)
print(problem_stack.solve_later)
print(problem_stack.quantity())
problem_stack.show_problems()