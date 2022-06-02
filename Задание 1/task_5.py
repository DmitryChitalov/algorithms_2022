"""
������� 5. �� ����������� ������� ������ �� ������
���������� ����������� �����-��������� "������ �������".
�� ����� ���������� ������� � ������ � ��� ���������� ���������� ��������
����� ������ ���������� ������� � ����� ������.
��������� ������ ��������������� ������� ���������� ������.
�������� ����� ������ ���������� ��� ���������� ����������
������ ���������� ��������.
����� ���������� ���������, ��������� �� ������ �� ��������� ���������.
����������: ����� ��� ����������� ������ �������!
--���������� �� �������� � ��������, ������������� �� �����
--�������� ������ ������ ����� ����������� ����������� ������ ������� �������
� ������ ������ (lst = [[], [], [], [],....]).
"""

class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """������������, ��� ������� ������� ����� ��������� � ����� ������"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

class MyStackClass:
    def __init__(self, limit):
        self.limit = limit # ���������� ������ �������� �����
        self.elems = [] # ������� ����
        self.list_elems = [] # ���� ������

    def is_empty(self):
        return self.elems == [] and self.list_elems == []

    def push_in(self, el):
        # ���� ������� ���� ��������, ��������� ��� � ���� ������ � ������� ����� ������� ����
        if len(self.elems) == self.limit:
            self.list_elems.append(self.elems)
            self.elems = []
        self.elems.append(el)

    def pop_out(self):
        # ���� ������� ���� ������, ������� �� ����� ������ ���������� ������� � �������� � ���
        # ���� ���� ������ ������, ���������� None 
        if self.elems == []:
            if self.list_elems == []:
                return None
            else:
                self.elems = self.list_elems.pop()
        return self.elems.pop()

    def get_val(self):
        # ���� ������� ���� ������, ������� �� ����� ������ ���������� � �������� � ���
        # ���� ���� ������ ������, ���������� None 
        if self.elems == []:
            if self.list_elems == []:
                return None
            else:
                self.elems = self.list_elems.pop()
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.list_elems) * self.limit + len(self.elems)

stack = MyStackClass(3)
print(stack.get_val())
stack.push_in(11)
print(stack.get_val())
stack.push_in(12)
stack.push_in(13)
stack.push_in(14)
print(stack.stack_size())
print(stack.get_val())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
