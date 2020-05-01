def add_numbers(*args):
    total = 0
    for a in args:
        total += a
        
    print("total pluss", total)
        

    
add_numbers(1)
add_numbers(1,2,3,4,5,5,6,7,8,9)
add_numbers(123,456,789)
add_numbers(3,3)


'''
* brukes for å ta med så mange variabler man vill. Args er bare navnet på variable
men det er common practice å bruke args for en variabel som tar med alle variablene.
'''


'''
    for a in args:
        total *= a
        
    print("total gange", total)
HMMMMMM?
'''
