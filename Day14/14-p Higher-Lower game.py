# logo
import art
# game data
from game_data import data
import random
from replit import clear

# start


# random person
def person(p):
  p = random.choice(data)
  name = p["name"]
  follower = p["follower_count"]
  description = p["description"]
  country = p["country"]
  p = [name, description, country, follower]
  return p


def winner():
  if follower1 > follower2:
    return 'A'
  elif follower1 < follower2:
    return 'B'


# game_over
game_over = False
score = 0
p = person("p")

while not game_over:
  print(art.logo)
  # score
  if score > 0:
    print(f"You're right! Current score: {score}.")
  # A, B

  print(f"Compare A: {p[0]}, {p[1]}, from {p[2]}")
  follower1 = p[3]

  print(art.vs)

  p = person("p")
  print(f"Against B: {p[0]}, {p[1]}, from {p[2]}")
  follower2 = p[3]

  more_follower = winner()

  # input()
  answer = input("Who has more followers? Type 'A' or 'B': ")
  print(answer)
  # finish
  if answer == more_follower:
    score += 1
    clear()
  elif answer != more_follower:
    game_over = True
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")

