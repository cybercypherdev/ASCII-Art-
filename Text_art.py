from pyfiglet import figlet_format
from colorama import Fore, Style, init
import sys
import random

# Initialize colorama
init(autoreset=True)

fonts = [
    "Standard",
    "Banner",
    "Ghost",
    "Larry3d",
    "Mini",
    "Shadow",
    "Banner3-D",
    "Doh"
]

print(figlet_format('Codart', font='big'))

# Define a list of colors to use
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def colored_figlet_format(text, font):
    ascii_art = figlet_format(text, font=font)
    colored_art = ""
    for char in ascii_art:
        if char.strip():  # Only color non-whitespace characters
            color = random.choice(colors)
            colored_art += color + char
        else:
            colored_art += char
    return colored_art

def generate():
    try:
        word = input("Enter a word to convert to art: ")
        for i, fontname in enumerate(fonts, 1):
            print(f"{i}. {fontname}")

        fontnumber = int(input("Enter the number of a font you want to try out: "))
        if fontnumber < 1 or fontnumber > len(fonts):
            raise ValueError("Invalid font number. Please select a number from the list.")

        choosenfont = fonts[fontnumber - 1]
        print(colored_figlet_format(word, font=choosenfont))

    except ValueError as ve:
        print(f"Error: {ve}")
        generate()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    redo = input("Do you want to redo (y/n): ")
    if redo.lower() == 'y':
        generate()
    else:
        sys.exit()

try:
    generate()
except KeyboardInterrupt:
    print("\nProgram exited by user.")
    sys.exit()
