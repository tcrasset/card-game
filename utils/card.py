class Symbol:
    def __init__(self, icon: str):
        if icon in ["♥", "♦"]:
            self.color = "red"
        else:
            self.color = "black"

        self.icon = icon


class Card(Symbol):
    def __init__(self, value: str, icon: str):
        super().__init__(icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} {self.icon}"
