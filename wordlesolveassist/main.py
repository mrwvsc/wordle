from solver import WordleSolver
from wordle import parse_verdict
from words import load_all_words

def main():
    word_list = load_all_words("allwords.txt")
    print(f"Loaded {len(word_list)} words: {word_list[:5]}")  # Debugging line
    solver = WordleSolver(word_list)

    while True:
        guess = input("Enter your guess (e.g., 'train'): ").strip().lower()
        verdict_str = input("Enter the verdict (e.g., 'gybyg'): ").strip().lower()
        verdict = parse_verdict(verdict_str)
        print(f"Parsed verdict: {verdict}")  # Debugging line

        possible_words = solver.filter_words(guess, verdict)
        print(f"Filtered words: {possible_words}")  # Debugging line
        print(f"Possible words: {', '.join(possible_words)}")

        # Write the possible words to a text file
        with open("filtered_words.txt", "w") as file:
            file.write("\n".join(possible_words))
        print("Filtered words have been written to 'filtered_words.txt'.")

if __name__ == "__main__":
    main()