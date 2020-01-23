import json
import random
import constants


TOTAL_KANJI = 2200

def main():
    generate_files()
    to_study = load_json_file("to-study.json")
    studied = load_json_file("studied.json")
    edited = False

    while True:
        print_intro_prompt()
        choice = input("> ").lower()[0]
        
        # Get Remaining Count
        if choice == "c":
            amount_studied = len(studied)
            print("\nStudied:", amount_studied)
            print("Remaining:", constants.TOTAL_KANJI - amount_studied)
            pause()

        # Get Kanji
        if choice == "g":
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
                    pause()
                    break
                else:
                    print("Sorry, please try again.")

        # Save and Quit
        if choice == "q":
            if edited:
                save(to_study, studied)
            print("Goodbye =)")
            return


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


def pause():
    input()

def print_intro_prompt():
    print("What do you want to do?")
    print("    c) Get number of kanji remaining")
    print("    g) Get a random kanji index")
    print("    q) Quit")


def print_get_kanji_prompt(kanji_index):
    print(f"\nKanji: {kanji_index}")
    print("    a) Add to studied")
    print("    s) Skip")
    print("    q) Quit")


def generate_files():
    # 1 -> 2200
    kanji_indices = list(range(1, 2200 + 1))
    
    with open("to-study.json", "w", encoding="utf-8") as f:
        json.dump(kanji_indices, f, ensure_ascii=False, indent=4)
    
    with open("studied.json", "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)


def get_first_char_lower(text):
    return lower(text)[0]

main()