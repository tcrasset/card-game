

class Symbol:
    def __init__(self, icon):
        if icon in ['♥', '♦']:
            self.color = "red"
        else:
            self.color = "black"

        self.icon = icon


class Card(Symbol):
    def __init__(self, value, icon):
        super().__init__(icon)
        self.value = value

    def __str__(self):
        return f"{self.value} {self.icon}"
        