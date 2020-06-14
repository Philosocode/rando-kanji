#!/usr/local/bin/python3
from constants import ( TOTAL_KANJI )


def get_choice():
    choice = input("> ").lower()
    choice = choice.strip()

    if len(choice) == 0: 
        return " "

    return choice[0]


def pause(message = ""):
    input(message)


def print_intro_prompt(index, kanji, meaning):
    print(f'\n[{index}] {kanji} "{meaning}"')
    print("    a) Add to studied")
    print("    n) Next\n")

    print("    c) Copy kanji to clipboard")
    print("    s) Skip kanji")
    print("    r) Get remaining number of kanji")
    print("    q) Quit")


def print_remaining_kanji(studied, skipped):
    print("\nStudied:", studied)
    print(f"Remaining: {TOTAL_KANJI - studied - skipped}")
    print(f"Skipped: {skipped}")