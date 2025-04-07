import random 
low = 1
high = 100
guesses = 0 
number = random.randint(low, high)
while True: #while loop starts and will stop after you have guessed correct number
    guess = int(input(f"enter the number you think is most fit accordin to you {low}-{high}:-"))
    guesses +=1 #increases the value of guesses by 1 everytime a guess is made 
    if guess < number:
     print(f"{guess} is to low")
    elif guess > number  :
     print(f"{guess} is too high ")
    else:
     print(f"{guess} is correct answer")
     break
print(f"this round took you {guesses} guesses")