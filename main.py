#!/usr/bin/python
import json
import random
import pyperclip

# Custom Modules
from constants import ( TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI )
import file_handler
import io_handler
import validator


def main():
    validator.validate_study_files()
    
    to_study, studied = file_handler.get_study_files()
    kanji_dict = file_handler.get_kanji_dict()

    while True:
        io_handler.print_intro_prompt()
        choice = io_handler.get_choice()

        # Get Kanji Index
        if choice == "r":
            handle_get_kanji(to_study, studied, kanji_dict)
        
        # Get Remaining Count
        elif choice == "c":
            io_handler.print_remaining_kanji(studied)

        # Save and Quit
        elif choice == "q":
            handle_quit()

        else:
            handle_invalid_choice()


def handle_get_kanji(to_study, studied, kanji_dict):
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
            print(f"Sorry, {choice} is not a valid option. Please try again.")


def handle_quit():
    print("\nGoodbye =)")
    exit(0)


def handle_invalid_choice():
    input("ERROR: Choice not recognized. Please try again.")


main()