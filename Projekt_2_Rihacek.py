
"""
projekt_2_Rihacek.py: druhý projekt do Engeto Online Python Akademie

author: Martin Řiháček
email: martinrihacek@seznam.cz
discord: mMartin95

""" 


import random


#Nadefinování náhodného čísla:

def generate_random_4_digit_number(): #Ale na první pozici nesmí být 0!!!
    #function that generate random 4 digit number
    first_position_number =  "".join(random.choice("123456789"))
    other_positions_number = "".join(random.sample("0123456789", 3))
    number = first_position_number + other_positions_number
    return number

random_number = generate_random_4_digit_number() 
print(random_number)

## Úvodní text:

line = "_"*75

 #2.
    #Pozdravit uživatele

print("Hi there!")
print(line)

    #Vypsat text

print("I've generated a random 4 digit number for you.","\nLet's play a bulls and cows game.")
print(line)

#3 and 4.
# Tady musí být funkce while: dokud budou platit chyby, tak to tam bude psát 
#Musí zde být funkce while, protože potřebuji, aby to furt házelo enter number:

while True:
    guess_number = input("Enter the number:")
    print(line)
    if guess_number.isdigit() and len(guess_number) < 4:
        print("Your number is shorter than 4 digits. Correct it.")
    elif guess_number.isdigit() and len(guess_number) > 4:
        print("Your number is longer than 4 digits. Correct it.")
    elif not guess_number.isdigit():
        print("Your number contains not numeric attribute. Correct it.")
    elif guess_number.isdigit() and guess_number[0] == "0":
        print("Your number must not start with 0. Correct it.")
    elif len(set(guess_number)) != len(guess_number):
        print("Your number contains duplicates. Correct it.") #Set totiž nemůže obsahovat duplikáty
    else: 
        break


print(">>> " + guess_number)

#5.

#definovná funkce:

def check_bulls_cows(guess_number, random_number):
    number_of_attempts = 0
    while guess_number != random_number:
        bull, cow = 0, 0
        number_of_attempts = number_of_attempts + 1
        for i in range(len(guess_number)):
            if guess_number[i] == random_number[i]: 
                bull += 1                            
            if guess_number[i] in random_number: 
                cow += 1
        
        bull_plural = "bull" if bull == 1 else "bulls"
        cow_plural = "cow" if cow == 1 else "cows"
    
        print(f"{bull} {bull_plural}, {cow} {cow_plural}")
        guess_number = input("Enter a new number: ")

    print(f"Correct, you've guessed the right number in {number_of_attempts} attempts.")

print(check_bulls_cows(guess_number, random_number))