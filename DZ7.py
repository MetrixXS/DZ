class MyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current_number = 0
        return self

    def  __next__(self):
        if self.current_number <= self.n:
            result = self.current_number
            self.current_number += 1
            return result
        else:
            raise StopIteration

    def count_down(self):
        for i in range(self.n, -1, -1):
            yield i

    def multiplier(self, m):
        def multiply(y):
            return y * m
        return multiply


    def print_result(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Результат: {result}")
            return result
        return wrapper

if __name__ == "__main__":
    my_iter = MyIterator(5)

    print("Ітератор:")
    for num in my_iter:
        print(num, end=" ")
    print("\nГенератор:")
    for num in my_iter.count_down():
        print(num, end=" ")

    print("\n\nЗамикання multiplier:")
    multiply_by_2 = my_iter.multiplier(2)
    print(multiply_by_2(24), multiply_by_2(8))

