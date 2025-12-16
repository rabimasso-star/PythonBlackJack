import random
import tkinter as tk
from tkinter import messagebox

def create_deck():
    deck = []
    for value in range(2, 11):
        deck.extend([value] * 4)
    deck.extend([10] * 12)
    deck.extend([11] * 4)
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.start_game()

        self.player_label = tk.Label(root, text="")
        self.player_label.pack()

        self.dealer_label = tk.Label(root, text="")
        self.dealer_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack()

        self.update_labels()

    def start_game(self):
        self.deck = create_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.game_over = False

    def update_labels(self):
        self.player_label.config(
            text=f"Dina kort: {self.player_hand} (Summa: {calculate_score(self.player_hand)})"
        )
        self.dealer_label.config(
            text=f"Datorns synliga kort: {self.dealer_hand[0]}"
        )

    def hit(self):
        if self.game_over:
            return

        self.player_hand.append(self.deck.pop())
        self.update_labels()

        if calculate_score(self.player_hand) > 21:
            messagebox.showinfo("Förlust", "Du gick över 21!")
            self.end_game()

    def stand(self):
        if self.game_over:
            return

        while calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())

        player_score = calculate_score(self.player_hand)
        dealer_score = calculate_score(self.dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            result = "Du vinner!"
        elif player_score < dealer_score:
            result = "Datorn vinner!"
        else:
            result = "Oavgjort!"

        messagebox.showinfo(
            "Resultat",
            f"Dina kort: {self.player_hand} ({player_score})\n"
            f"Datorns kort: {self.dealer_hand} ({dealer_score})\n\n{result}"
        )

        self.end_game()

    def end_game(self):
        self.game_over = True
        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")

root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()
