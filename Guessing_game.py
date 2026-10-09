import random

print("=" * 40)
print("  WELCOME TO GUESSING GAME - Gayathri!")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
score = 100

print("\nI have selected a number between 1 to 100")
print(f"You have {max_attempts} chances only!")
print("Let's start!\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Please enter between 1 to 100 only!")
            continue
        
        if guess == secret_number:
            print("\n" + "=" * 40)
            print(f"CONGRATULATIONS! You won!")
            print(f"Secret number is {secret_number}")
            print(f"You guessed in {attempts} attempts")
            print(f"Your final score: {score}")
            print("=" * 40)
            break
            
        elif guess < secret_number:
            diff = secret_number - guess
            if diff <= 5:
                print("Very close! Slightly low, go little high!")
            elif diff <= 15:
                print("Close! Too low! Try higher!")
            else:
                print("Too low! Go much higher!")
            score -= 10
            
        else:
            diff = guess - secret_number
            if diff <= 5:
                print("Very close! Slightly high, go little low!")
            elif diff <= 15:
                print("Close! Too high! Try lower!")
            else:
                print("Too high! Go much lower!")
            score -= 10
            
        remaining = max_attempts - attempts
        print(f"Remaining chances: {remaining}, Score: {score}\n")
        
    except ValueError:
        print("Please enter only numbers!")

else:
    print("\n" + "=" * 40)
    print("GAME OVER! You lost!")
    print(f"The secret number was {secret_number}")
    print("Better luck next time Gayathri!")
    print("=" * 40)
