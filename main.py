#!/usr/bin/python
import json
import random

# Custom Modules
import constants
import file_handler


def main():
    setup()

    return

    to_study = load_json_file("to_study.json")
    studied = load_json_file("studied.json")
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


def setup():
    # Check that `studied.json` and `to-study.json` exist
    # If they don't, create them
    missing_files = file_handler.check_files_exist("to_study.json", "studied.json")

    # Both files exist. Good to go
    if len(missing_files) == 0: 
        return

    # Missing both. Create them them
    if len(missing_files) == 2:
        file_handler.create_study_files()
        return
    
    # Missing one of them. Use existing file to re-create the missing one
    if len(missing_files) == 1:
        file_handler.generate_missing_file(missing_files[0])


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


def load_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def save(to_study, studied):
    to_study.sort()
    studied.sort()

    with open("to-study.json", "w", encoding="utf-8") as f:
        json.dump(to_study, f, ensure_ascii=False, indent=4)
    
    with open("studied.json", "w", encoding="utf-8") as f:
        json.dump(studied, f, ensure_ascii=False, indent=4)


def print_intro_prompt():
    print("=== MAIN MENU ===")
    print("What do you want to do?")
    print("    c) Get number of kanji remaining")
    print("    g) Get a random kanji index")
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


main()