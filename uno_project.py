class cards:
    def __init__(self, color, c_set = []):
        self.color = color
        self.c_set = c_set

    def create_cards(self):
        for x in range(0, 10):
            if x !=0:
                self.c_set.append((x,self.color))
                self.c_set.append((x,self.color))
            else:
                self.c_set.append((x,self.color))
        for x in range(2):
            self.c_set.append(("reverse",self.color))
            self.c_set.append(("skip",self.color))
            self.c_set.append(("draw_2",self.color))
            self.c_set.append(("wild",self.color))
            self.c_set.append(("wild",self.color))
            self.c_set.append(("wild_draw4",self.color))
            self.c_set.append(("wild_draw4",self.color))

red_cards = cards("red")
red_cards.create_cards()
blue_cards = cards("blue")
blue_cards.create_cards()
green_cards = cards("green")
green_cards.create_cards()
yellow_cards = cards("yellow")
yellow_cards.create_cards()
print(green_cards.c_set)

    