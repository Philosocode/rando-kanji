#!/usr/bin/python
import json
import os
from constants import ( TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI )


# PUBLIC
def create_json_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(sorted(data), f, ensure_ascii=False, indent=4)
        print(f"SAVED: {file_name}.")


def get_study_files():
    to_study = _load_json_file(TO_STUDY_FILE)
    studied = _load_json_file(STUDIED_FILE)

    return [to_study, studied]


def generate_missing_files(missing_files):
    if len(missing_files) == 1:
        print(f"ERROR: Missing file: {missing_files[0]}. Regenerating...")
        _generate_missing_file(missing_files[0])
    else:
        print("ERROR: Missing both files. Regenerating...")
        _create_study_files()


def save_files(to_study, studied):
    """ `to_study` and `studied` should be lists of indices """
    create_json_file(TO_STUDY_FILE, to_study)
    create_json_file(STUDIED_FILE, studied)
    print("Files saved.")


# PRIVATE
def _create_kanji_indices():
    """ Return a list with the numbers 1 to TOTAL_KANJI """
    return list(range(1, TOTAL_KANJI + 1))


def _create_study_files():
    """ Create to_study & studied JSON files """
    kanji_indices = _create_kanji_indices()
    create_json_file(TO_STUDY_FILE, kanji_indices)
    create_json_file(STUDIED_FILE, [])


def generate_missing_file(missing_file_name):
    """ Use `to_study` file to generate `studied` (and vice versa) """
    
    # Approach: add all indices to `to_study` if they're not in `studied`
    if missing_file_name == TO_STUDY_FILE:
        from_file = STUDIED_FILE
    elif missing_file_name == STUDIED_FILE:
        from_file = TO_STUDY_FILE
    else:
        print(f"ERROR: Invalid file - {missing_file_name}.")
        exit(1)

    # Load indices from existing file
    # e.g. if missing `studied`, load from `to_study`
    existing_indices = _load_json_file(from_file)
    all_indices = _create_kanji_indices()
    
    # Generate new list with indices not present in `kanji_indices`
    indices_to_save = [n for n in all_indices if n not in existing_indices]

    # Create new file with missing indices
    create_json_file(missing_file_name, indices_to_save)

    print(f"Re-created {missing_file_name}.")


def _load_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)