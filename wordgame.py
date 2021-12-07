"""Final Project"""

import sys
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.letters = set(["b","c","d","f","g","h","j","k","l","m","n","p","q", "r","s","t","v","w","x","y","z"])
        self.score= 0
        self.words = []
        
        self.scoring = {"a" :0, "b": 1, "c": 1, "d": 1, "e":0, "f" : 1, "g": 1, "h": 1, "i": 0,
                        "j": 1, "k" : 1, "l": 1, "m" : 1, "n": 1, "o": 0, "p": 1, "q": 3, "r": 1,
                      "s": 1, "t": 1, "u": 0, "v": 3, "w": 2, "x": 4, "y": 4, "z": 5}
    
    def check_win(self):
        if len(self.letters) == 0:
            return True 
        return False
    
    def check_if_valid(self, word, dictionary):
        word = word.lower() 
        if word not in dictionary:
            print("That word is not in the dictionary. Please try again.")
            return False
        for letter in word:
            if letter not in self.letters and letter not in "aeiou":
                print("You've already used that letter. Please try again.")
                return False
        return True
    
    def input_word(self, word, dictionary):
        if self.check_if_valid(word, dictionary):
            for letter in word:
                self.letters.discard(letter)
                self.score += self.scoring.get(letter)
            self.words.append(word)

    def play_game(self, dictionary):
        print(self.name +", press enter when you're ready.")
        enter = input()
        if enter == '\n':
            start = time.time()
            while time.time() -  start < 6:
                print(self.name +" enter a word! These are your current letters ")
                print(self.letters)
                word = input()
                self.input_word(word, dictionary)
            print(self.name+ " your time is up. You got " + str(self.score) + " points.\n")

            
                        
def start_game():
    print ("Welcome to Brain Scramble\n")
    name1 = input("Please enter your name, player 1!\n")
    name2 = input("Please enter your name, player 2!\n")
    player1 = Player(name1)
    player2 = Player(name2)
    print("""Let's begin the game! You have 60 seconds to create as many words 
          as possible, with the letters given. You can used any of the vowels an
          unlimited amount of time, however consonants may only be used once. You can repeat available consonants in a given word. 
          Your goal is to use every single letter in the alphabet at least once! 
          Good luck! \n""")
    return player1, player2

def import_dictionary(filename):
    dictionary = set(line.strip() for line in open(filename))
    return dictionary


def main():
    dictionary = import_dictionary("english3.txt")
    player1, player2 = start_game()
    player1.play_game(dictionary)
    player2.play_game(dictionary)

    if player1.score > player2.score:
        print("Player 1 wins!!")
    elif player2.score > player1.score:
        print("Player 2 wins!!")
    else:
        print("It's a Tie!!")

if __name__== "__main__":
    main()
    
    
    
    
  
    
    
    
    
        
        
        
        
        