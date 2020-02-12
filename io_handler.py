#!/usr/bin/python
from constants import ( TOTAL_KANJI )


def get_choice():
    return input("> ").lower()[0]


def pause():
    input()


def print_get_kanji_prompt(kanji_index):
    print("\n=== RANDO KANJI ===")
    print(f"Kanji: {kanji_index}")
    print("    a) Add to studied")
    print("    s) Skip")
    print("    q) Quit")


def print_intro_prompt():
    print("\n=== MAIN MENU ===")
    print("What do you want to do?")
    print("    r) Get a random kanji index")
    print("    c) Get count of remaining kanji")
    print("    q) Quit")


def print_remaining_kanji(studied):
    amount_studied = len(studied)
    print("\nStudied:", amount_studied)
    print("Remaining:", TOTAL_KANJI - amount_studied)
    pause()