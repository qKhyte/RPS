# Importing libraries
import time
import random

# Game introduction
print('Rock 🪨')
time.sleep(0.5)
print('Paper 📄')
time.sleep(0.5)
print('Scissors ✂️')
time.sleep(0.5)
print('SHOOT❗️')
time.sleep(2)

# Player choice to see if they want to play
playerPlay = ''
def playerPlayLoop():
  global playerPlay
  playerPlay = input('Rock Paper Scissors!\nMr. RPS challenges you to a Rock Paper Scissors game, do you accept? (Y/N)\n>>>  ')
playerPlayLoop()

# Dictionary to see stats.
stats = {
  'wins': 0,
  'losses': 0,
  'ties': 0
}

# If statements 
if playerPlay.lower() == 'y':
  
  def game():

    def playAgain():
      playAgainCheck = input('Do you want to play again? (Y/N)\n>>> ')
      playAgainCheck = playAgainCheck.lower()
      if playAgainCheck == 'y':
        game()
      elif playAgainCheck == 'n':
        print(f"Good game!\nWins: {stats['wins']}\nLosses: {stats['losses']}\nTies: {stats['ties']}") 
      else:
        playAgain()

    aiChoices = ['r', 'p', 's']
    aiChoice = aiChoices[random.randint(0,2)]
    playerChoice = input('Pick your move! (R/P/S)\n>>> ')
    playerChoice = playerChoice.lower()
  
    if playerChoice == 'r': 
      
      if aiChoice == 'r':
        
        stats['ties'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Tie!')
        time.sleep(1)
        playAgain()
        
      elif aiChoice == 'p':
        
        stats['losses'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Lost!')
        time.sleep(1)
        playAgain()

      elif aiChoice == 's':
        
        stats['wins'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Won!')
        time.sleep(1)
        playAgain()
      
    elif playerChoice == 'p': 

      if aiChoice == 'r':
        
        stats['wins'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Won!')
        time.sleep(1)
        playAgain()
        
      elif aiChoice == 'p':
        
        stats['ties'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Tie!')
        time.sleep(1)
        playAgain()

      elif aiChoice == 's':
        
        stats['losses'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Lost!')
        time.sleep(1)
        playAgain()

    elif playerChoice == 's':
      
      if aiChoice == 'r':
        
        stats['losses'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Lost!')
        time.sleep(1)
        playAgain()
        
      elif aiChoice == 'p':
        
        stats['wins'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Won!')
        time.sleep(1)
        playAgain()

      elif aiChoice == 's':

        stats['ties'] += 1
        print('Rock 🪨')
        time.sleep(0.5)
        print('Paper 📄')
        time.sleep(0.5)
        print('Scissors ✂️')
        time.sleep(0.5)
        print('SHOOT❗️')
        time.sleep(2)
        print('Tie!')
        time.sleep(1)
        playAgain()
  game()
elif playerPlay.lower() == 'n':
  time.sleep(0.5)
  print('No fun!')
  time.sleep(2)
  exit()
else:
  playerPlayLoop()
