#!/usr/bin/python
from constants import ( TOTAL_KANJI )

import file_handler


def validate_data_file():
    # Create valid "master" file to validate against
    valid_dict = file_handler.create_kanji_dict()
    to_check = file_handler.get_kanji_dict()
    is_valid = True

    for kanji in valid_dict:
        # Make sure `to_check` contains all the kanji
        # If not, add it to `to_check`
        if kanji not in to_check:
            print(f"Missing kanji from data file: {kanji}.")
            to_check[kanji] = valid_dict[kanji]
            is_valid = False
        # Make sure indices match
        # If not, update index in `to_check`
        to_check_index = to_check[kanji]["index"]
        valid_index = valid_dict[kanji]["index"]
        if to_check_index != valid_index:
            print(f"{kanji}: updating index from {to_check_index} to {valid_index}.")
            to_check[kanji["index"]] = valid_dict[kanji]["index"]
            is_valid = False
        
        # Make sure meanings match
        # If not, update index in `to_check`
        to_check_meaning = to_check[kanji]["meaning"]
        valid_meaning = valid_dict[kanji]["meaning"]
        if to_check_meaning != valid_meaning:
            print(f"{kanji}: updating meaning from {to_check_meaning} to {valid_meaning}.")
            to_check[kanji["meaning"]] = valid_dict[kanji]["meaning"]
            is_valid = False
    
    if is_valid:
        print("Data file validated. No errors found.")