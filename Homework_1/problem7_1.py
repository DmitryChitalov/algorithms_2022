class Deque:
    def __init__(self):
        self.letters = []

    def is_empty(self):
        return self.letters == []

    def front_add(self, letter):
        self.letters.append(letter)

    def back_add(self, letter):
        self.letters.insert(0, letter)

    def front_remove(self):
        return self.letters.pop()

    def back_remove(self):
        return self.letters.pop(0)

    def lenght(self):
        return len(self.letters)
