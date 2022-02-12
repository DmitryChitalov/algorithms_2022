class NoDgt(Exception):
    def __init__(self, txt):
        self.txt = txt

class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.lc = None
        self.rc = None

    def insert(self, new_node):
        if self.lc is None:
            if self.rc is not None:
                if new_node <= self.rc:
                    self.lc = BinaryTree(new_node)
                else:
                    self.lc = self.rc
                    self.rc = BinaryTree(new_node)
            else:
                self.rc = BinaryTree(new_node)
        else:
            if self.rc is not None:
                if new_node <= self.rc:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.lc = self.lc
                    self.lc = tree_obj
                else:
                    self.lc = self.rc
                    tree_obj = BinaryTree(new_node)
                    tree_obj.rc = self.rc
                    self.rc = tree_obj
            else:
                self.rc = BinaryTree(new_node)

    def get_right_child(self):
        return self.rc

    def get_left_child(self):
        return self.lc

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        try:
            if self.root is not None:
                return self.root
            else:
                raise NoDgt('')
        except NoDgt:
            return None

# Трудно дорабатывать изначально не очень удобное решение, тут легче с нуля написать,
# но Вы скажете, мол, в задании по-другому написано было сделать