from solver import WordleSolver
from wordle import parse_verdict
from words import load_all_words

def main():
    word_list = load_all_words("allwords.txt")
    print(f"Loaded {len(word_list)} words: {word_list[:5]}")
    solver = WordleSolver(word_list)

    guesses = []
    verdicts = []

    while True:
        while True:
            guess = input("Enter your guess (e.g., 'train'): ").strip().lower()
            if guess not in word_list:
                print("that isnt even a word. try again")
            else:
                break
        verdict_str = input("Enter the verdict (e.g., 'gybyg'): ").strip().lower()
        verdict = parse_verdict(verdict_str)
        print(f"Parsed verdict: {verdict}")

        guesses.append(guess)
        verdicts.append(verdict)

        # Start with the full word list and filter with all guesses/verdicts
        possible_words = word_list
        for g, v in zip(guesses, verdicts):
            possible_words = solver.filter_words(g, v, possible_words)

        print(f"Possible words: {', '.join(possible_words)}")

        with open("filtered_words.txt", "w") as file:
            file.write("\n".join(possible_words))
        print("Filtered words have been written to 'filtered_words.txt'.")

if __name__ == "__main__":
    main()