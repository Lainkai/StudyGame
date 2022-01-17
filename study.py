import csv
import os
import random

import tkinter as tk
from tkinter import filedialog


class StudyGame:

    table = list()
    score = 0
    possible_score = 0
    streak = 0
    highest_streak = 0

    def __init__(self, table):
        self.load_table(table)
    
    def load_table(self,reader):
        for row in reader:
            self.table.append(row)

    def handle_game_loop(self):
        clear_screen()
        self.handle_display_score()
        #Pick the word row to conjugate
        word = self.table[random.randrange(1,len(self.table)-1)]
        #pick the conjugate to grade
        conjugate_index = random.randrange(1,len(word)-1)
        correct_answer = word[conjugate_index]
        prompt_word = word[0]
        prompt_word_conjugation = self.table[0][conjugate_index]
        answer = input("What is the {} of {}: ".format(prompt_word_conjugation,prompt_word)).strip()
        self.possible_score += 1

        if answer == correct_answer:
            self.streak += 1
            self.score+=1
            print("Correct!")
        else:
            print("Incorrect. {} was the answer.".format(correct_answer))
            self.streak = 0
        
        if self.streak > self.highest_streak:
            self.highest_streak = self.streak

        input("Press enter to continue.")

        
    def handle_display_score(self):
        print("Total Score: {} / {} | Streak: {} | High Streak: {}".format(self.score, self.possible_score,self.streak, self.highest_streak))

def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')

if __name__ == "__main__":
    clear_screen()
    
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(initialdir="./")
    root.destroy()

    if(file == ''):
        clear_screen()
        print("Please enter a file next time.")
        exit()
    
    print("Reading "+file)
    with open(file,encoding='utf8',newline='') as table:
        game = StudyGame(csv.reader(table, delimiter=',', quotechar='|'))
        while(True):
            try:
                game.handle_game_loop()
            except KeyboardInterrupt:
                clear_screen()

                print("Thank you for playing!")
                exit()