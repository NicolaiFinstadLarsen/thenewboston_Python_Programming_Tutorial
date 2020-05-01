def allowed_dating_age(my_age = int(input("Hvor gammel er du? "))):
    
    girls_age = my_age/2 + 7
    return girls_age

lower_limit = allowed_dating_age()

print("Du kan date de som er over: ", lower_limit, "år gamle")  