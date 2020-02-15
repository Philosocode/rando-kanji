#!/usr/bin/python
import json
import os
import pickle

from constants import ( TO_STUDY_FILE, STUDIED_FILE, KANJI_DATA_FILE, KANJI_DICT_FILE, TOTAL_KANJI )


# PUBLIC
def create_json_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"SAVED: {file_name}.")


def get_study_files():
    to_study = _load_json_file(TO_STUDY_FILE)
    studied = _load_json_file(STUDIED_FILE)

    return [to_study, studied]


def get_kanji_dict():
    """ index => [kanji, meaning]  """
    if not _file_exists(KANJI_DICT_FILE):
        print("Creating kanji dict.")
        _create_kanji_dict()
    
    return _load_pickle_file(KANJI_DICT_FILE)


def generate_missing_files(missing_files):
    if len(missing_files) == 1:
        print(f"ERROR: Missing file: {missing_files[0]}. Regenerating...")
        _generate_missing_file(missing_files[0])
    elif len(missing_files) >= 2:
        print("ERROR: Missing both files. Regenerating...")
        _create_study_files()


def save_files(to_study, studied):
    """ `to_study` and `studied` should be lists of indices """
    create_json_file(TO_STUDY_FILE, sorted(to_study))
    create_json_file(STUDIED_FILE, sorted(studied))
    print("Files saved.")


# PRIVATE
def _create_kanji_indices():
    """ Return a list with the numbers 1 to TOTAL_KANJI """
    return list(range(1, TOTAL_KANJI + 1))


def _create_kanji_dict():
    kanji_lines = _get_lines_from_file(KANJI_DATA_FILE)
    kanji_dict = {}

    for line in kanji_lines:
        split_line = line.split(":")
        idx, kanji, meaning, *rest = split_line

        kanji_dict[int(idx)] = [kanji, meaning]
    
    _create_pickle_file(KANJI_DICT_FILE, kanji_dict)


def _create_pickle_file(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def _create_study_files():
    """ Create to_study & studied JSON files """
    kanji_indices = _create_kanji_indices()
    create_json_file(TO_STUDY_FILE, kanji_indices)
    create_json_file(STUDIED_FILE, [])


def _file_exists(file_name):
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        return False

    return True


def _get_lines_from_file(file_name):
    with open(file_name, "r") as f:
        return [line.rstrip("\n") for line in f]


def _generate_missing_file(missing_file_name):
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


def _get_missing_study_files():
    """ Check if study files exist. Return a List containing the names of the files that don't exist """
    not_found_files = []

    for file_name in [TO_STUDY_FILE, STUDIED_FILE]:
        if not _file_exists(file_name):
            not_found_files.append(file_name)

    return not_found_files


def _load_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def _load_pickle_file(file_name):
    with open(file_name, "rb") as f:
        data = pickle.load(f)
        return data