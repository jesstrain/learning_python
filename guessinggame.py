

target = 8
guessed = False 
guesses = 3

print("Can you guess my number? It is between 1 and 10. You have three guesses.")
while not guessed and guesses > 0:
        
    my_number = int(input("Enter your guess: "))
    guesses = guesses - 1
    if my_number == target:
        guessed = True

if guessed:
    print("Correct! You have guessed my number!")
else:
    print("You have ran out of guesses!")