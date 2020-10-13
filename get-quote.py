import random

file="quotes.txt"

def quote_generator():

  f = open(file)
  quotes = f.readlines()
  f.close()

  first_random_item, second_random_item = random.sample(quotes, 2)
  print (first_random_item, second_random_item,sep="",end="")

def add_quote():
  user_quote=input("Write your quote and hit enter:\n")

  adding=open(file,"a")
  adding.write(user_quote+"\n")
  adding.close()
  print("You have added", user_quote, "to quotes.txt")

while True:
  single_quote=input("Do you want to (i) insert a quote, (g) generate two random quotes or (e) exit?\n")
  if single_quote == "i":
    add_quote()
  elif single_quote == "g":
    quote_generator()
  elif single_quote == "e":
    exit()
  else:
    print ("Invalid option, please try again...\n")