from getwords import randomword

with open("allwords.txt", "r", encoding="utf-8") as f:
    rawWords = f.readlines()
    words = [line.strip() for line in rawWords if line.strip()]

class Wordle: # in class for future editing (idk if i'll be doing that)
    def wordle():
        secret_word = randomword()
        attempts = 6
        
        print("New game begun.")
        while attempts > 0:
            guess = input("enter your guess: ").strip().lower()
            if len(guess) != 5:
                print("guess must be 5 characters")
                continue

            if guess not in words:
                print("that isn't even a word")
                continue

            if guess == secret_word:
                print(f"ok u win. word was {secret_word}")
                break

            feedback = []
            for char in range(5):
                if guess[char] == secret_word[char]:
                    feedback.append("🟩")
                elif guess[char] in secret_word:
                    feedback.append("🟨")
                else:
                    feedback.append("🟥")
            

            print(f"Feedback: " + " ".join(feedback))
            attempts -= 1
            print(f"attempts remaining: {attempts}")
        
        if attempts <= 0:
            print(f"u lost. word was {secret_word}")

if __name__ == "__main__":
    while True:
        x = input("Would you like to start a new game? [Y/N]: ").strip().lower()
        if x == "y":
            Wordle.wordle()
        elif x == "n":
            print("exiting program")
            exit()
        elif x == "yes":
            Wordle.wordle()
        elif x == "no":
            print("exiting program")
            exit()
# made this if statement a bit too long, "y" and "yes" wasn't working. 