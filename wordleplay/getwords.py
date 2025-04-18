# notes for the reader: if you are reading this, make sure to run this file first to check for any possible
# mishaps in the code
import random

def randomword():
    try: # for debug      
        with open("allwords.txt", "r", encoding="utf-8") as f: # change allwords.txt according to your needs
            rawWords = f.readlines()
            words = [line.strip() for line in rawWords if line.strip()] 
            if not words:
                raise ValueError("The word list is empty.")
            return random.choice(words)   
    except FileNotFoundError: # error handling if file isn't found. 
        raise FileNotFoundError("The file 'allwords.txt' was not found.")
    except Exception as e: # error handling
        raise RuntimeError(f"An error occurred: {e}")
    

if __name__ == "__main__": # explicitly runs if getwords.py is run by itself.
    randomword()