from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

dictionary = {}
other_user = "yes"

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

finished = False
while not finished:
  name = input("What is your name?")
  price = int(input("What is your bid price? : $"))
  dictionary[name] = price
  other_user = input("Are there other users who want to bid? yes or no ").lower()
  if other_user == "no":
    finished = True
  elif other_user == "yes":
    clear()
    
highest_bidder(dictionary)
