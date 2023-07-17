txt = input("Greeting: ").strip().title() # User enters some kind of greeting

if txt.startswith("Hello"): # If the user types "Hello" then get $0
    print("$0")
elif txt.startswith("H"): # If the user types some greeting who starts with "H", then get $20
    print("$20")
else:
    print("$100") # If the user types another kind of greeting, wins $100

#Harvard cs50 #6 
