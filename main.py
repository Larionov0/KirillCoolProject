class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_smth(self, text):
        """
            Говорит что-то от имени кого-то
        """
        print('-' * 30)
        print(f"{self.name}: '{text}'")
        print('-' * 30)

    def grow_up(self):
        self.age += 1
        print(f"{self.name} подрос на год. Теперь ему {self.age} лет")


h = Human('Bob', 20)
h.say_smth('I love pizza')
h.grow_up()
