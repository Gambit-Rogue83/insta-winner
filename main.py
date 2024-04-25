from art import logo, vs
from game_data import data
from random import choice, sample
from replit import clear
score = 0
contender_a, contender_b = sample(data, 2)
# def matchup(cont1, cont2):
  
    

def unpack(data):
    """Unpacks the data from a dictionary and returns the name, description and country of the data"""
    name = data['name']
    description = data['description']
    country = data['country']
    # followers = data['follower_count']
    return f"{name}, a(n) {description}, from {country}."
  
def followers(dic1, dic2):
  """compares the followers of two entities and determines the higher of the two"""
  fan_a = dic1['follower_count']
  fan_b = dic2['follower_count']
  if fan_a > fan_b:
    return ['a', dic1]
  else:
    return ['b', dic2]

def insta_winner(points, defender, competitor):
  clear()
  print(logo)
  if points > 0:
    print(f"You're right! Current score: {points}")
  print("Compare A: "  + unpack(defender))
  
  print(vs)
  print("Against B: " + unpack(competitor))
  
  winner = followers(defender, competitor)
  vote = input("Who has more followers? Type 'A' or 'B': ").lower()
  if vote == winner[0]:
    defender = competitor
    competitor = choice(data)
    points += 1
    insta_winner(points, defender=defender, competitor=competitor)
  else:
    print(f"Sorry, that's wrong. Final score: {points}")

insta_winner(score, contender_a, contender_b)

