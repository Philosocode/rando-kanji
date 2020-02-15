#!/usr/bin/python
import json
import random
import pyperclip

# Custom Modules
from constants import ( TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI )
import file_handler
import io_handler


def main():
    # [kanji] => [idx, meaning]
    kanji_dict = file_handler.get_kanji_dict()
    to_study, studied = generate_study_sets(kanji_dict)

    while True:
        io_handler.print_intro_prompt()
        choice = io_handler.get_choice()

        # Get Kanji Index
        if choice == "r":
            handle_get_kanji(kanji_dict)
        
        # Get Remaining Count
        elif choice == "c":
            handle_get_remaining_kanji()

        # Save and Quit
        elif choice == "q":
            handle_quit()

        else:
            handle_invalid_choice(choice)


def generate_study_sets(kanji_dict):
    to_study = set()
    studied = set()

    return [to_study, studied]


def handle_get_kanji(kanji_dict):
    get_new_kanji = True

    while True:
        # Select random EL/index from `to_study`
        if get_new_kanji:
            random_index = random.choice(to_study)
            pyperclip.copy(random_index)
            get_new_kanji = False
        
        [kanji, meaning] = kanji_dict[random_index]

        io_handler.print_get_kanji_prompt(random_index, kanji, meaning)
        choice = io_handler.get_choice()

        # Add index to studied
        if choice == "a":
            to_study.remove(random_index)
            studied.append(random_index)
            file_handler.save_files(to_study, studied)
            get_new_kanji = True

        elif choice == "s":
            get_new_kanji = True
            continue

        elif choice == "q":
            return

        else:
            handle_invalid_choice(choice)


def handle_get_remaining_kanji():
    io_handler.print_remaining_kanji(studied)


def handle_invalid_choice(choice):
    input(f'ERROR: Choice "{choice}" not recognized. Please try again.')


def handle_quit():
    print("\nGoodbye =)")
    exit(0)


main()