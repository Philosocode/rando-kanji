#!/usr/bin/python
import json
import random

# Custom Modules
from constants import ( TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI )
import file_handler
import io_handler
import validator


def main():
    validator.validate_study_files()
    
    to_study, studied = file_handler.get_study_files()

    while True:
        io_handler.print_intro_prompt()
        choice = io_handler.get_choice()

        # Get Kanji Index
        if choice == "r":
            handle_get_kanji(to_study, studied)
        
        # Get Remaining Count
        if choice == "c":
            io_handler.print_remaining_kanji(studied)

        # Save and Quit
        if choice == "q":
            handle_quit()

        else:
            handle_invalid_choice()


def handle_get_kanji(to_study, studied):
    get_new_kanji = True

    while True:
        # Select random EL/index from `to_study`
        if get_new_kanji:
            random_index = random.choice(to_study)
            get_new_kanji = False

        io_handler.print_get_kanji_prompt(random_index)
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
            print()
            return

        else:
            print(f"Sorry, {choice} is not a valid option. Please try again.")


def handle_quit():
    print("\nGoodbye =)")
    exit(0)


def handle_invalid_choice():
    input("ERROR: Choice not recognized. Please try again.")

main()