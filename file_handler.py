#!/usr/bin/python
import json
import os
from constants import (
    TO_STUDY_FILE, STUDIED_FILE, TOTAL_KANJI
)
from validators import (
    has_valid_indices
)

# PUBLIC
def check_for_missing_files():
    """ Check if `to_study` and `studied` exist """
    return _check_files_exist(TO_STUDY_FILE, STUDIED_FILE)


def generate_missing_files(missing_files):
    if len(missing_files) == 1:
        _generate_missing_file(missing_files[0])
    else:
        _create_study_files()


def get_study_files():
    to_study = _load_json_file(TO_STUDY_FILE)
    studied = _load_json_file(STUDIED_FILE)

    return [to_study, studied]


def validate_study_files():
    """ Ensure `to_study` and `studied` files are valid """
    to_study, studied = get_study_files()

    for n in to_study:
        if n < 0 or n > 2200:
            return _create_study_files()

    for n in studied:
        if n < 0 or n > 2200:
            return _create_study_files()

    to_study_unique_indices = list(set(to_study))
    studied_unique_indices = list(set(studied))

    # Check for duplicate indices in each file
    if len(to_study) + len(studied) != TOTAL_KANJI:
        _delete_file(STUDIED_FILE)
        _create_json_file(TO_STUDY_FILE, to_study_unique_indices)
        _generate_missing_file(STUDIED_FILE)

    # No common index found in both files: good to go
    if len(to_study_unique_indices) + len(studied_unique_indices) == TOTAL_KANJI:
        return
    
    # There was 1 or more index in both files... not good
    # Re-create `studied` based on `to_study`
    _delete_file(STUDIED_FILE)
    _create_json_file(TO_STUDY_FILE, to_study_unique_indices)
    _generate_missing_file(STUDIED_FILE)
    return


# PRIVATE
def _check_files_exist(*file_names):
    """ Check if the file(s) passed exist. Return a List containing files that don't exist
    """
    not_found = []

    for file_name in file_names:
        try:
            f = open(file_name)
            f.close()
        except FileNotFoundError:
            not_found.append(file_name)

    return not_found


def _create_json_file(file_name, data):
    """ Create a JSON file with data passed """
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"CREATED: {file_name}")


def _create_kanji_indices():
    """ Return a list with the numbers 1 to 2200 """
    return list(range(1, 2200 + 1))


def _create_study_files():
    """ Create to_study & studied JSON files """
    kanji_indices = _create_kanji_indices()
    _create_json_file(TO_STUDY_FILE, kanji_indices)
    _create_json_file(STUDIED_FILE, [])


def _delete_file(file_name):
    os.remove(file_name)
    print(f"DELETED: {file_name}")


def _generate_missing_file(missing_file_name):
    """ Use `to_study` file to generate `studied` (and vice versa) """
    
    # Approach: add all indices to `to_study` if they're not in `studied`
    if missing_file_name == TO_STUDY_FILE:
        from_file = STUDIED_FILE
    elif missing_file_name == STUDIED_FILE:
        from_file = TO_STUDY_FILE

    # Load indices from existing file (e.g. missing `studied` then load from `to_study`)
    existing_indices = _load_json_file(from_file)
    all_indices = _create_kanji_indices()
    
    # Generate new list with indices not present in `kanji_indices`
    indices_to_save = [n for n in all_indices if n not in existing_indices]

    # Create new file with missing indices
    _create_json_file(missing_file_name, indices_to_save)

    print(f"Re-created {missing_file_name}.")


def _load_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)