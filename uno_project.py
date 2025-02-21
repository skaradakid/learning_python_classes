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
            return self.c_set

class player():
    def __init__(self, name, hand=[]):
        self.hand = hand
        self.name = name

    def play(self):
        print(f"{self.name} these are your cards:")
        for x in self.hand:
            print(f"{self.hand.index(x)}-{x}")

        print("\nplay a card")
        pick = int(input("choose by index or input pick to draw a card: "))
        if pick == "pick":
            self.hand.append(drop_zone[-1])
            drop_zone.pop(-1)
        while True:
            try:
                print(self.hand[pick])
                break
            except:
                print("choose a valid number")
                pick = int(input("choose by index: "))
        return pick

class computer:
    def __init__(self, name="npc", hand=[]):
        self.hand = hand
        self.name = name

    def play(self):
        for x in self.hand:
            if x[0] == drop_zone[-1][0] or x[1] == drop_zone[-1][1]:
                print(x)
                return x
        self.hand.append(drop_zone[-1])
        drop_zone.pop(-1)

def revs_order(lst):
    return(lst[::-1])
karabo = player("karabo")
cpu = computer()
def game(*players: object):
    players_lst = [players]
    print(revs_order(players_lst))
    print(players_lst)
    # red_cards = cards("red")
    # blue_cards = cards("blue")
    # green_cards = cards("green")
    # yellow_cards = cards("yellow")

    # def card_deck():
    #     all_cards = green_cards.create_cards() + yellow_cards.create_cards() + red_cards.create_cards() + blue_cards.create_cards()
    #     shuffe = list(set(all_cards))
    #     return shuffe

    # shuffled_cards = card_deck()
    # drop_zone = []
game(karabo,cpu)
    