from letter import Letter


class Word:

    def __init__(self):
        self.letters = []

    def __repr__(self):
        return f'{self.letters}'

    def encode(self, word):
        auxiliar = []
        position = 0
        for each in word:
            position += 1
            if not each in auxiliar:
                self.letters.append(Letter(each, [position]))
                auxiliar.append(each)
            else:
                for letter in self.letters:
                    if letter.letter == each:
                        letter.positions.append(position)