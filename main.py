#!/usr/bin/python
import json
import random
import pyperclip
from KanjiManager import KanjiManager

# Custom Modules
from constants import ( TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI )
import file_handler
import io_handler


def main():
    """
    [
        studied: Set, 
        to_study: Set, 
        dict: [kanji] => { 
            meaning: string,
            idx: string,
            studied: bool
        }
    ]
    """
    kanji_manager = get_kanji_manager()

    while True:
        io_handler.print_intro_prompt()
        choice = io_handler.get_choice()

        # Get Kanji Index
        if choice == "r":
            handle_get_kanji(kanji_manager)
        
        # Get Remaining Count
        elif choice == "c":
            handle_get_remaining_kanji(kanji_manager)

        # Save and Quit
        elif choice == "q":
            handle_quit()

        else:
            handle_invalid_choice(choice)


def get_kanji_manager():
    # [kanji] => [idx, meaning]
    kanji_dict = file_handler.get_kanji_dict()
    
    to_study = set()
    studied = set()

    for kanji in kanji_dict:
        is_studied = kanji_dict[kanji]["studied"]

        if is_studied:
            studied.add(kanji)
        else:
            to_study.add(kanji)

    return KanjiManager(to_study, studied, kanji_dict)


def handle_get_kanji(kanji_manager):
    get_new_kanji = True

    [to_study, studied, kanji_dict] = kanji_manager

    while True:
        # Select random EL/index from `to_study`
        if get_new_kanji:
            kanji = get_random_kanji(to_study)
            pyperclip.copy(kanji)
            get_new_kanji = False
        
        index = kanji_dict[kanji]["index"]
        meaning = kanji_dict[kanji]["meaning"]

        io_handler.print_get_kanji_prompt(index, kanji, meaning)
        choice = io_handler.get_choice()

        # Add index to studied
        if choice == "a":
            kanji_dict[kanji]["studied"] = True
            to_study.remove(kanji)
            studied.add(kanji)
            file_handler.save(kanji_dict)
            get_new_kanji = True

        elif choice == "s":
            get_new_kanji = True
            continue

        elif choice == "q":
            return

        else:
            handle_invalid_choice(choice)


def get_random_kanji(kanji_set):
    # https://stackoverflow.com/a/24949742
    return random.choice(tuple(kanji_set))


def handle_get_remaining_kanji(kanji_manager):
    remaining_kanji = len(kanji_manager.studied)
    io_handler.print_remaining_kanji(remaining_kanji)


def handle_invalid_choice(choice):
    input(f'ERROR: Choice "{choice}" not recognized. Please try again.')


def handle_quit():
    print("\nGoodbye =)")
    exit(0)


main()