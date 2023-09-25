import random
print("""                                                                                     
 ,----.   ,--. ,--.,------. ,---.   ,---.                                            
'  .-./   |  | |  ||  .---''   .-' '   .-'                                           
|  | .---.|  | |  ||  `--, `.  `-. `.  `-.                                           
'  '--'  |'  '-'  '|  `---..-'    |.-'    |                                          
 `------'  `-----' `------'`-----' `-----'                                           
  ,--.  ,--.                ,--.  ,--.,--. ,--.,--.   ,--.,-----.  ,------.,------.  
,-'  '-.|  ,---.  ,---.     |  ,'.|  ||  | |  ||   `.'   ||  |) /_ |  .---'|  .--. ' 
'-.  .-'|  .-.  || .-. :    |  |' '  ||  | |  ||  |'.'|  ||  .-.  \|  `--, |  '--'.' 
  |  |  |  | |  |\   --.    |  | `   |'  '-'  '|  |   |  ||  '--' /|  `---.|  |\  \  
  `--'  `--' `--' `----'    `--'  `--' `-----' `--'   `--'`------' `------'`--' '--'""")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

i = random.randint(1,100)


def guess(a):
  n = a
  for _ in range(a):
    print(f"You have {n} attempts remaining to guess the number.")
    global i
    n -= 1
    answer = int(input("Make a guess: "))
    if i == answer:
      print(f"You got it! The answer was {i}.")
      break
    elif i > answer:
      print("Too low.")
    else:
      print("Too high")
  if n == 0:
    print("You've run out of guesses, you lose.")
    
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
   
if difficulty == "easy":
  guess(10)
elif difficulty == "hard":
  guess(5)