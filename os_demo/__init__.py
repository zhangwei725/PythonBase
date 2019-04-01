class Test:
    a = 0

    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


if __name__ == '__main__':
    t = Test()
    t.age = 16
    print(t.age)
    t.name = 'hello'
