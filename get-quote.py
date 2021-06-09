import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last_quote = len(quotes)
  random_nr = random.randint(0,last_quote)
  print(quotes[random_nr])

if __name__== "__main__":
  primary()
