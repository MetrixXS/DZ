from urllib.parse import SplitResult


class StringIterator:
    def __init__(self, strings):
        self.strings = strings
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.strings):
            color = self.strings[self.index]
            self.index += 1
            return color
        else:
            raise StopIteration

strings_iter = StringIterator("slim, medium, large")

for string in strings_iter:
    print(string)

