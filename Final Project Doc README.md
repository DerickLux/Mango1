# Mango1
The name of our game is called Brain Scramble.
The concept of our game is that the players will be using every consonant in the alphabet once, and vowels as many times as the player wants 
to create actual exisitng words as much as the player can in a given time. Each alphabet will have a given score and based on the words the
player created, the scores will be added up and whoever has the highest score wins.
#### Files needed to run the project:
- english3.txt (a text file containing existing words from the dictionary)
- wordgame.py (a program file that contains the code for the game to run)
#### For our code, we have used the following functions: 
- __init__()
- check_win()
- check_if_valid()
- input_word()
- play_game()
- start_game()
- import_dictionary()
- main()
- if__main__=="__main__"
#### Function explanation, 
Our code starts with __init__() function which allows us to construct all the attributes we need such as the player's name, the alphabets, scores, and words.
Next, we use the check_win() function to check which player will win at the end of the game. Next, we have the check_if_valid() function which allows us to
check whether the words that the players created are actually exisiting words by matching the created words to our word bank and if the words match the ones 
in the word bank, it will be valid to count towards the score. Next, we used the input_word() function that allows us to store the created valid words and remove
the used alphabets from the alphabet set and let the players continue the game. Next we have the play_game() function which will set a timer to the game and whenever
the time is over, the game stops. Next, we have the start_game() function which is one our main function in the game. This function will actually start the entire 
game by giving the instructions of the game and make the players to put their names. Next we have the import_dictionary() function which allows us to import the 
dictionary that we will be using for our word bank. Next we have the main() function which starts the game, imports the "english3.txt" file (our word bank) as a dictionary, 
assign the dictionary to each of the players to check the validity of the words created, and compare the score for each player to decide who is the winner. Lastly 
we have our if__main__=="__main__" function to run our entire code for the game.
#### To run the code,
- 1. Open terminal
- 2. Type: cd Mango1 (enter)
- 3. Type: python3 wordgame.py (enter)
- 4. Follow the instructions of the game shown in the terminal
#### Sources & Authors
- check_if_valid(), input_word() from Kyungho
- __init__(), check_win(), play_game(), start_game(), import_dictionary(), main(), if__main__=="__main__" from Maya
