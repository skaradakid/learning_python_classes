class cards:
    def __init__(self, color, c_set = []):
        self.color = color
        self.c_set = c_set

    def numbered_cards(self):
        for x in range(1, 8):
            self.c_set.append((x,self.color))
            self.c_set.append((x,self.color))

    def sepecial_cards(self):
        pass

    