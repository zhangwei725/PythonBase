class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.__sex = '男'

    def _show(self):
        return '{}:{}'.format(self._name, self._age)


if __name__ == '__main__':
    user = User(name='小明', age=20)
    # print(user._age)
    # print(user._show())
    # print(user.__sex)