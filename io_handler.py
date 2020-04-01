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
    print("    s) Skip\n")

    print("    c) Copy kanji to clipboard")
    print("    r) Get remaining number of kanji")
    print("    q) Quit")


def print_remaining_kanji(studied):
    print("\nStudied:", studied)
    pause(f"Remaining: {TOTAL_KANJI - studied}")