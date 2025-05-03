import random
number = random.randint(1, 100) # Change the range fir 10 to 100
guess = int(input())
if guess == number:
 print("You win!")
else:
 print(f"Wrong! The number was {number}")

#second editing of the code
while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break
