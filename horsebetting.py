import random
import time

horses = []


class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.money = 100

    def place_bet(self, horse, bet):
        return int(horse.odds * bet)

    def winner(self):
        if self.money <= 0:
            print("You have no money left")


class Horse:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.chance = random.uniform(0.5,1)
        self.odds = 1 - self.chance
        self.speed = round(self.odds*4)
        self.bet = 0
        self.position = 0
        horses.append(self)

    def get_horse_pos(self):
        return self.position

    def get_horse_color(self):
        return self.color[0]

    def __str__(self):
        return self.name


class Track:
    def __init__(self, track_length):
        self.horse_num = len(horses)
        self.length = track_length

    def check_winner(self):
        for horse in horses:
            if horse.position >= self.length:
                print("{} is the winner".format(horse.name))
                return horse

    def print_track(self):
        for horse in horses:
            print(str(horse.name) + ": ")
            for space in range(self.length):
                if space == horse.get_horse_pos():
                    print(horse.name[0], end="")
                else:
                    print("_", end="")
            print()

    def round(self):
        counter = 0
        round_over = False
        winner = None
        while not round_over:
            time.sleep(1)
            print("\nRound {}".format(counter))
            self.print_track()
            winner = self.check_winner()
            if winner:
                return winner
            for horse in horses:
                horse.position += random.choice(range(horse.speed, 5))


            counter += 1

    def calculate_odds(self):
        for horse in horses:
            print("Chance of winning for {0} ({1}): {2:.4}".format(horse.name, horse.color, horse.odds))


def main():
    horse1 = Horse("Mickey", "Red")
    horse2 = Horse("Peter", "Blue")
    horse3 = Horse("Bob", "Pink")
    horse4 = Horse("Chad", "Brown")
    track = Track(50)

    player = Player()

    for i in range(0, 2):
        if player.money > 0:
            track.calculate_odds()
            horse = input("What horse would you like to bet on: ")
            bet = int(input("Place your bets (current: {}): ".format(player.money)))
            player.money -= bet
            winner = track.round()
            print(winner)
            if str(winner.name) == horse:
                winnings = int((1+winner.odds) * bet)
                player.money += winnings
                print("You won {}! You have {}".format(winnings, player.money))
            else:
                print("You lost! You have {}".format(player.money))
        else:
            print("You lost")
            break

game = main()