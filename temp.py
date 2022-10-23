class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    # Переопределите метод describe().
    def describe(self, full=False):
        if full == True:
            return (
                    f'Попугай {self.name} — заметная птица'
                    f'Окрас ее перьев -{self.color}'
                    f'а размер - {self.size}.'
                    f'Интересный факт: попугаи чувствуют ритм,'
                    f'а вовсе не бездумно двигаются под музыку.'
                    f'Если сменить композицию,'
                    f'то и темп движений птицы изменится.'
                   )
        else:
            return super().describe(full)

class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size=False)
        self.genus = genus
    # Переопределите метод describe().
    def describe(self, full):
        if full == True:
            return (
                    f'Размер пингвина {self.name} из рода {self.genus}'
                    f'Интересный факт: однажды группа геологов-'
                    f'разведчиков похитила пингвинье яйцо, и их'
                    f'принялась преследовать вся стая, не пытаясь,'
                    f'впрочем, при этом нападать. Посовещавшись,'
                    f'похитители вернули птицам яйцо, и те отстали.'
                    f'то и темп движений птицы изменится.'
                   )
        else:
            return super().describe(full)


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))