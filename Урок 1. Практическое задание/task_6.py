"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class ToDo_List:
  def __init__(self):
    self.new_tasks = dict()
    self.tasks_in_work = dict()
    self.ready_tasks = dict()

  def add_task(self, task_name: str(), task: str()):
    if task_name not in self.new_tasks and task_name not in self.tasks_in_work:
      self.new_tasks[task_name] = task
    else:
      pass

  def task_complete(self, task_name: str()):
    if task_name in self.new_tasks or task_name in self.tasks_in_work:
      task = self.new_tasks[task_name] if task_name in self.new_tasks else self.tasks_in_work[task_name]
      if task_name not in self.ready_tasks:
        self.ready_tasks[task_name] = task
        if task_name in self.new_tasks:
          del self.new_tasks[task_name]
        else:
          del self.tasks_in_work[task_name]
      else:
        pass
    else:
      pass

  def task_in_work(self, task_name: str()):
    if task_name in self.new_tasks:
      if task_name not in self.tasks_in_work:
        self.tasks_in_work[task_name] = self.new_tasks[task_name]
        del self.new_tasks[task_name]
      else:
        pass
    else:
      pass

  def show_tasks(self):
    if self.new_tasks:
      print('-' * 60)
      print('NEW TASKS')
      print('-' * 60)
      for t in self.new_tasks:
        print(t, ':', self.new_tasks[t])
    else:
      print('NO ONE NEW TASK!')
    print('\n')
    if self.tasks_in_work:
      print('-' * 60)
      print('TASKS IN WORK')
      print('-' * 60)
      for t in self.tasks_in_work:
        print(t, ':', self.tasks_in_work[t])
    else:
      print('NO ONE TASK IN WORK!')
    print('\n')

  def show_ready_tasks(self):
    if self.ready_tasks:
      print('-' * 60)
      print('READY TASKS')
      print('-' * 60)
      for t in self.ready_tasks:
        print(t, ':', self.ready_tasks[t])
    else:
      print('NO ONE TASK IS READY!')
    print('\n')

  def the_clean_slate_protocol(self):
    print('\x1B[3mJ: All wrapped up here, sir. Will there be anything else?\x1B[23m')
    print('\x1B[3mT: You know what to do.\x1B[23m')
    print('\x1B[3mJ: The Clean Slate Protocol, sir?\x1B[23m')
    print('\x1B[3mT: Screw it, it\'s Christmas. Yes, yes.\x1B[23m')
    self.new_tasks.clear()
    self.tasks_in_work.clear()
    self.ready_tasks.clear()


if __name__ == '__main__':
  Tasks = ToDo_List()
  Tasks.add_task('first_task', 'Test! Test! Test!')
  Tasks.show_tasks()
  Tasks.show_ready_tasks()
  Tasks.task_in_work('first_task')
  Tasks.add_task('second_task', 'PupiPu')
  Tasks.task_complete('second_task')
  Tasks.add_task('third_task', 'I\'m Banana Man!')
  Tasks.show_tasks()
  Tasks.show_ready_tasks()
  Tasks.the_clean_slate_protocol()
