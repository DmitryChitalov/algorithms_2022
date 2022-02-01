
#Задание 5. На закрепление навыков работы со стеком
class StackClass:
    def __init__(self):
        self.elems=[]
        self.newstack=[]

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)
        if len(self.elems)>5:
            self.newstack.append(el)


    def pop_out(self):
        return self.elems.pop()
    def get_val(self):
        return self.elems[len(self.elems)-1]
    def stack_size(self):
        return len(self.elems)
    def newstack_size(self):
        return len(self.newstack)



if __name__ == '__main__':
   abc=StackClass()
   abc.push_in(5)
   abc.push_in(2)
   print(abc.is_empty())
   print(abc.stack_size())
   abc.push_in(2)
   abc.push_in(2)
   abc.push_in(2)
   abc.push_in(2)
   abc.push_in(2)
   abc.push_in(2)
   abc.push_in(2)
   print(abc.stack_size())
   print(abc.newstack_size())
   print(abc.newstack)