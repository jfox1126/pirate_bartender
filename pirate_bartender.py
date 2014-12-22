questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

like_list = {}

def ask_likes():
  def convert_boolean(x):
    y = raw_input(questions[x])
    if y.lower() == "yes" or y.lower() == "y":
      y = True
    else:
      y = False
    return y
  global like_list
  like_list = {
    "strong": convert_boolean("strong"),
    "salty": convert_boolean("salty"),
    "bitter": convert_boolean("bitter"),
    "sweet": convert_boolean("sweet"),
    "fruity": convert_boolean("fruity"),
  }
  print like_list

import random

def drink_maker():
  ask_likes()
  drink_ingredients = []
  def add_ingredients(x):
    if like_list[x] == True:
      random_ingredient = random.choice(ingredients[x])
      drink_ingredients.append(random_ingredient)
  add_ingredients("strong")
  add_ingredients("salty")
  add_ingredients("bitter")
  add_ingredients("sweet")
  add_ingredients("fruity")
  print drink_ingredients
  
if __name__ == "__main__":
  drink_maker()