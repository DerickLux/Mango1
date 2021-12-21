"""Final Project"""

import sys
import time

class Player:
    """
    This class is designed to represent a player in the game as well as 
    establish the known game. This class willestablish the name of the player as
    well as constitute the known words and letters that will be used in the game.
    
    Attributes:
        name (str): first name of the player
        word (str): word crafted from letters in the set dictionary
        dictionary: a file containing a dictionary with every word in the 
                    english dictionary
    
    Methods:
        check_win: this method will check who of the two players wins the game.
        check_if_valid: this method will check if the word created is valid or 
                        not.
        input_word: this method will input the known word into the dictionary to 
                    calculate scoring, and figure out which letters are left for
                    the players to use. 
        play_game: this method illustrates how the game will begin. 
    
    """
    def __init__(self, name):
        """ This method constructs all the attributes needed to establish the 
        player name, the set of letters, the score, and the words. 
        
        Parameters:
            Name (str): first name of player 
        """
        self.name = name
        self.letters = set(["b","c","d","f","g","h","j","k","l","m","n","p","q", "r","s","t","v","w","x","y","z"])
        self.score= 0
        self.words = []
        
        self.scoring = {"a" :0, "b": 1, "c": 1, "d": 1, "e":0, "f" : 1, "g": 1, "h": 1, "i": 0,
                        "j": 1, "k" : 1, "l": 1, "m" : 1, "n": 1, "o": 0, "p": 1, "q": 8, "r": 1,
                      "s": 1, "t": 1, "u": 0, "v": 6, "w": 2, "x": 4, "y": 4, "z": 5}
    
    def check_win(self):
        """This method checks which player will win the game at the end. """
        if len(self.letters) == 0:
            return True 
        return False
    
    def check_if_valid(self, word, dictionary):
        """ This method checks if the word crafted by either one of the players 
        is valid. If the word is not valid, meaning it doesn't follow the rules
        for crafting a word, the game will print a message saying the player 
        must try again.
        
        Attributes:
            word: a word created by the letters allowed in the set
            dictionary: a file containing a dictionary containing all the words 
                        in the english language 
        """
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
        """This method checks whether the word is valid, and then removes said 
        letters from the dictionary in order to pursue with the game. 
        
        Attributes:
            word: a word created by the letters allowed in the set
            dictionary: a file containing a dictionary containing all the words 
                        in the english language 
        """
        if self.check_if_valid(word, dictionary):
            for letter in word:
                self.letters.discard(letter)
                self.score += self.scoring.get(letter)
            self.words.append(word)

    def play_game(self, dictionary):
        """This method sets up how the game is played in terms of time, as well 
        as instructions.
        
        Attributes:
            dictionary: a file containing a dictionary containing all the words 
                        in the english language 
        """
        print(self.name +", press enter when you're ready.")
        enter = input()
        if enter == "":
            start = time.time()
            while time.time() -  start < 60:
                print(self.name +" enter a word! These are your current letters ")
                print(self.letters)
                word = input()
                self.input_word(word, dictionary)
            print(self.name+ " your time is up. You got " + str(self.score) + " points.\n")

            
                        
def start_game():
    """This method starts the game and details the instructions in order to play
    correctly. It also takes note of the player names and brings the entire game 
    together.
    """
    print ("Welcome to Brain Scramble\n")
    name1 = input("Please enter your name, player 1!\n")
    name2 = input("Please enter your name, player 2!\n")
    player1 = Player(name1)
    player2 = Player(name2)
    print("""Let's begin the game! You have 60 seconds to create as many words 
          as possible, with the letters given. You can use all vowels an
          unlimited amount of times, however if you use a consonant you can not
          use it again. You can use a letter twice in a given word. 
          Your goal is to use every single letter in the alphabet at least once! 
          Good luck! \n""")
    return player1, player2

def import_dictionary(filename):
    """This method imports the dictionary from the exterior file."""
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
    
    
    
    
  
    
    
    
    
        
        
        
        
        