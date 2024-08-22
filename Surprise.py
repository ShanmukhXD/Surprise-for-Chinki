import time
import sys

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def print_cake():
    cake = [
        "     ,   ,   ,   ,   ,   ,   ,",
        "     |   |   |   |   |   |   |",
        "     =========================",
        "   | H A P P Y   B I R T H D A Y |",
        "  |         1 5   Y E A R S        |",
        " ====================================",
        " |                                   |",
        " |                                   |",
        "  ==================================="
    ]

    for line in cake:
        typewriter_effect(line)
        time.sleep(0.2)

def main():
    print("Welcome to your 15th Birthday Celebration Program!")
    print("\nLet's start the celebration...")
    print_cake()
    typewriter_effect(f"\n\n 🎉 Happy 15th Birthday, Chinki!")
    typewriter_effect("Wishing you a fantastic year filled with joy and success!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
