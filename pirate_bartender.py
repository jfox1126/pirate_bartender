import random

tastes = {
  "strong": {
    "question": "Do ye like yer drinks strong?",
    "ingredients": ["glug of rum", "slug of whisky", "splash of gin"]
  },
  "salty": {
    "question": "Do ye like it with a salty tang?",
    "ingredients": ["olive on a stick", "salt-dusted rim", "rasher of bacon"]
  },
  "bitter": {
    "question": "Are ye a lubber who likes it bitter?",
    "ingredients": ["shake of bitters", "splash of tonic", "twist of lemon peel"]
  },
  "sweet": {
    "question": "Would ye like a bit of sweetness with yer poison?",
    "ingredients": ["sugar cube", "spoonful of honey", "spash of cola"]
  },
  "fruity": {
    "question": "Are ye one for a fruity finish?",
    "ingredients": ["slice of orange", "dash of cassis", "cherry on top"]
  },
}

names = {
  "adjectives": ["Piercing", "Mellow", "Ragged", "Flourescent"],
  "nouns": ["Kraken", "Squid-tentacle", "Starfish", "Sperm whale"]
}

like_list = []  

def ask_likes():
  """Prompts user to provide input and creates a list of what they like"""
  print "Ahoy! Let me ask you a few questions to find you a drink. [Respond with 'yes' or 'y']." 
  for taste, question in tastes.iteritems():
    if raw_input(question["question"]).lower() in ["y", "yes"]:
      global like_list
      like_list.append(taste)
  print ""

def drink_maker():
  """Randomly selects ingredients based on user's tastes and gives the drink a name"""
  drink_ingredients = []
  for likes in like_list:
    random_ingredient = random.choice(tastes[likes]["ingredients"])
    drink_ingredients.append(random_ingredient)
  name = random.choice(names["adjectives"]) + " " + random.choice(names["nouns"])
  print "Then try a " + name + "! Just combine:"
  for i in range(len(drink_ingredients)):
    print "A " + drink_ingredients[i]
  print ""
  
def have_another():
  """Continues to ask user if s/he wants another until they say no"""
  x = raw_input("Do ye need another?")
  while x.lower() in ["y", "yes"]:
    drink_maker()
    x = raw_input("Do ye need another?")
  else:
    print "Glad I could help you!"

if __name__ == "__main__":
  ask_likes()
  drink_maker()
  have_another()