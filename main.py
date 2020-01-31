#!/usr/bin/python
import json
import random

# Custom Modules
import constants
from file_handler import (
    check_for_missing_files,
    generate_missing_files,
    get_study_files,
    validate_study_files
)


def main():
    # Validate study files
    missing_files = check_for_missing_files()
    if len(missing_files) == 0:
        validate_study_files()
    elif len(missing_files) > 0:
        generate_missing_files(missing_files)
    
    to_study, studied = get_study_files()
    print("=== to_study ===")
    print_list(to_study)
    print("=== studied ===")
    print_list(studied)

    return

    edited = False

    while True:
        print_intro_prompt()
        choice = get_choice()
        
        # Get Remaining Count
        if choice == "c":
            handle_show_remaining(studied)

        # Get Kanji
        if choice == "g":
            handle_get_kanji(to_study, studied)

        # Save and Quit
        if choice == "q":
            if edited:
                save(to_study, studied)
            print("\nGoodbye =)")
            exit(0)


def handle_show_remaining(studied):
    amount_studied = len(studied)
    print("\nStudied:", amount_studied)
    print("Remaining:", constants.TOTAL_KANJI - amount_studied)
    pause()


def handle_get_kanji(to_study, studied):
    while True:
        random_index = random.choice(to_study)
        print_get_kanji_prompt(random_index)
        get_kanji_choice = input("> ").lower()[0]

        # Add index to studied
        if get_kanji_choice == "a":
            to_study.remove(random_index)
            studied.append(random_index)
            save(to_study, studied)
            edited = True
        elif get_kanji_choice == "s":
            continue
        elif get_kanji_choice == "q":
            print()
            break
        else:
            print("Sorry, please try again.")


def save(to_study, studied):
    to_study.sort()
    studied.sort()

    with open(constants.TO_STUDY_FILE, "w", encoding="utf-8") as f:
        json.dump(to_study, f, ensure_ascii=False, indent=4)
    
    with open(constants.STUDIED_FILE, "w", encoding="utf-8") as f:
        json.dump(studied, f, ensure_ascii=False, indent=4)


def print_intro_prompt():
    print("=== MAIN MENU ===")
    print("What do you want to do?")
    print("    c) Get count of remaining kanji")
    print("    r) Get a random kanji index")
    print("    q) Quit")


def print_get_kanji_prompt(kanji_index):
    print("\n=== RANDO KANJI ===")
    print(f"Kanji: {kanji_index}")
    print("    a) Add to studied")
    print("    s) Skip")
    print("    q) Quit")


def get_choice():
    return input("> ").lower()[0]


def pause():
    input()


def print_list(data):

    if len(data) == 0:
        print("[]")
    else:
        res = ""

        for el in data:
            res += f"{str(el)}, "

        print(res)

main()