import time

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
red_cards = cards("red")
blue_cards = cards("blue")
green_cards = cards("green")
yellow_cards = cards("yellow")

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
karabo = player("karabo", hand=[])

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
cpu = computer(hand=[])

def revs_order(lst):
    return(lst[::-1])


def card_deck():
    all_cards = green_cards.create_cards() + yellow_cards.create_cards() + red_cards.create_cards() + blue_cards.create_cards()
    shuffe = list(set(all_cards))
    return shuffe

shuffled_cards = card_deck()
drop_zone = []
curse = 0

def game(*players: object):
    all_players = list(players)
    start = input("start game? ")
    if start.lower() != "yes":
        return print("game was ended")
    else:
        print("game between player and computer")
        print("dealing cards, please wait...")
        for y in range(1, 8):
            for x in all_players:
                x.hand.append(shuffled_cards.pop())
        drop_zone.append(shuffled_cards.pop())
        time.sleep(4)
        print(f"done!\ntop card is: {drop_zone[-1]}")
        while True:
            for x in all_players:
                if drop_zone[-1][0] in ["draw_2", "skip", "reverse", "wild_draw4"] and curse > 0:
                    if drop_zone[-1][0] == "draw_2":
                        x.hand.append(shuffled_cards.pop())
                        x.hand.append(shuffled_cards.pop())
                        curse -= 1
                    elif drop_zone[-1][0]  == "skip":
                        continue
                        curse -= 1
                    elif drop_zone[-1][0]  == "reverse":
                        all_players = revs_order(all_players)
                        curse -= 1
                    else:
                        x.hand.append(shuffled_cards.pop())
                        x.hand.append(shuffled_cards.pop())
                        x.hand.append(shuffled_cards.pop())
                        x.hand.append(shuffled_cards.pop())
                        curse -= 1
                else:
                    pass



game(karabo,cpu

)
    