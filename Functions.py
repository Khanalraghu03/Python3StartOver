#Define  a function
def my_function():
  print("Hello from a function")

# call the function
my_function()

print("\n")
def y_function(fname):
  print(fname + " Refsnes")

y_function("Emil")
y_function("Tobias")
y_function("Linus")

print("\n\n\n")
#function and methods are same: in java we call methods in python we call function
def chicken():
    print("cluck cluck")

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount, "Dollars")

chicken()
bitcoin_to_usd(3.99)
bitcoin_to_usd(1)
bitcoin_to_usd(7)

print("\n\n\n")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
