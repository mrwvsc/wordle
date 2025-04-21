def load_all_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []