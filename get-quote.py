import random

def primary():


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  first_random_item, second_random_item = random.sample(quotes, 2)
  print (first_random_item, second_random_item,sep="",end="")
  #print (second_random_item,end="")
if __name__== "__main__": 
  primary()
