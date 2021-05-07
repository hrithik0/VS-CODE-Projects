def boolean(bol):
    return bol


day = boolean(input("Is it a hot day ? True or False! "))
if day.lower() == "true":
    print("It's a hot day ")
    print("Drink plenty of water")
elif day.lower() == "false":
    print(" It's a cold day ")
    print("Wear warm clothes ")
else:
    print("It's a lovely day ")
